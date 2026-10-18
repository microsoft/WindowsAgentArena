"""Scripted model tests of Navi's real predict/dispatch/result-consumption path.

Only the model, screen-region extraction and remote MCP server are fixtures.
No Windows VM or live model credentials are needed.
"""
import io
import json
import os
import tempfile
import types
import unittest
from unittest.mock import patch

import requests
from PIL import Image
from requests.structures import CaseInsensitiveDict

from mm_agents.navi.agent import NaviAgent
from mm_agents.navi.web_search import (
    MAX_RESPONSE_BYTES, MCP_URL, PROTOCOL_VERSION, USER_AGENT,
    ParallelSearchClient, SearchError, resolve_search_provider,
)


SEARCH = {"name": "web_search", "arguments": {
    "objective": "Find VS Code keybinding removal instructions",
    "search_queries": ["VS Code remove keybinding"],
}}
SOURCE_URL = "https://code.visualstudio.com/docs/configure/keybindings?source=help#keyboard-shortcuts-editor"
FETCH = {"name": "web_fetch", "arguments": {"urls": [SOURCE_URL], "objective": "Remove a keybinding"}}
FINAL_PLAN = "```decision\nCOMMAND\n```\n```python\ncomputer.keyboard.press('escape')\n```"


def tool_plan(request):
    return "```web_tool\n" + json.dumps(request) + "\n```"


class Reply:
    def __init__(self, payload=None, status=200, content_type="application/json", raw=None):
        self.status_code = status
        self.headers = CaseInsensitiveDict({"Content-Type": content_type})
        self.body = raw if raw is not None else json.dumps(payload).encode()
        self.closed = False

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.closed = True

    def iter_content(self, chunk_size):
        yield self.body

    def iter_lines(self, **kwargs):
        yield from self.body.decode().splitlines()


class MCPServer:
    """Assert destination, transport controls and headers on every owned request."""
    def __init__(self, fault=None, sse=False):
        self.requests = []
        self.responses = []
        self.fault = fault
        self.sse = sse
        self.closed = False

    def post(self, url, **kwargs):
        assert url == MCP_URL
        assert kwargs["headers"]["User-Agent"] == USER_AGENT
        assert kwargs["headers"]["MCP-Protocol-Version"] == PROTOCOL_VERSION
        assert kwargs["headers"]["Accept"] == "application/json, text/event-stream"
        assert "Authorization" not in kwargs["headers"]
        assert kwargs["timeout"] == (5, 30)
        assert kwargs["allow_redirects"] is False
        assert kwargs["stream"] is True
        request = kwargs["json"]
        self.requests.append(request)
        method = request["method"]
        if method == "initialize":
            result = {"protocolVersion": PROTOCOL_VERSION, "capabilities": {"tools": {}}}
        elif method == "notifications/initialized":
            response = Reply(status=202)
            self.responses.append(response)
            return response
        elif method == "tools/list":
            result = {"tools": [{"name": name, "inputSchema": {"type": "object", "required": required}}
                                for name, required in [("web_search", ["objective", "search_queries"]),
                                                       ("web_fetch", ["urls"])]]}
        elif method == "tools/call":
            if self.fault:
                if isinstance(self.fault, BaseException):
                    raise self.fault
                result = self.fault
            else:
                result = {"structuredContent": {"results": [{"url": SOURCE_URL,
                          "excerpts": ["Right-click the keybinding and select Remove Keybinding."]}]}}
        else:
            raise AssertionError(method)
        payload = {"jsonrpc": "2.0", "id": request["id"], "result": result}
        if self.sse:
            raw = (": heartbeat\n\nevent: message\ndata: " + json.dumps(payload) + "\n\n").encode()
            response = Reply(content_type="text/event-stream", raw=raw)
        else:
            response = Reply(payload)
        self.responses.append(response)
        return response

    def close(self):
        self.closed = True


class ScriptedPlanner:
    system_prompt = "Original desktop prompt."

    def __init__(self, plans):
        self.plans = iter(plans)
        self.queries = []

    def plan(self, images, query):
        self.queries.append(query)
        return next(self.plans)


class NaviWebTests(unittest.TestCase):
    def setUp(self):
        image = Image.new("RGB", (32, 32), "white")
        stream = io.BytesIO()
        image.save(stream, format="PNG")
        self.obs = {"screenshot": stream.getvalue(), "window_title": "VS Code",
                    "window_names_str": "VS Code", "window_rect": [0, 0, 32, 32],
                    "computer_clipboard": "private clipboard text", "accessibility_tree": ""}
        obs_module = types.ModuleType("screen_fixture")
        obs_module.parser_to_prompt = lambda image, *args: (image, image, "VS Code screen")
        a11y = types.ModuleType("a11y_fixture")
        a11y.propose_ents = lambda tree: []
        self.modules = patch.dict("sys.modules", {
            "mm_agents.navi.screenparsing_oss.utils.obs": obs_module,
            "mm_agents.navi.a11y_demo": a11y,
        })
        self.modules.start()
        self.addCleanup(self.modules.stop)
        self.env = patch.dict(os.environ, {"PARALLEL_API_KEY": "must-not-send",
                                          "OPENAI_API_KEY": "must-not-send"}, clear=True)
        self.env.start()
        self.addCleanup(self.env.stop)

    def agent(self, plans, provider=None):
        planner = ScriptedPlanner(plans)
        with patch("mm_agents.navi.agent.GPT4V_Planner", return_value=planner):
            agent = NaviAgent(som_origin="a11y", model="gpt-4o", search_provider=provider)
        return agent, planner

    def predict(self, agent):
        return agent.predict("Remove the Ctrl+F Tree view Find keybinding", self.obs)

    def test_default_search_fetch_results_reach_desktop_planner(self):
        server = MCPServer()
        agent, planner = self.agent([tool_plan(SEARCH), tool_plan(FETCH), FINAL_PLAN])
        with patch("requests.Session", return_value=server):
            _, actions, logs, update = self.predict(agent)
        self.assertEqual(agent.search_provider, "parallel")
        self.assertEqual(actions, ["computer.keyboard.press('escape')\n"])
        self.assertIn("rects", update)
        self.assertEqual(len(logs["web_tools"]), 2)
        self.assertIn("Remove Keybinding", planner.queries[-1])
        self.assertIn(SOURCE_URL, planner.queries[-1])
        self.assertIn("Untrusted web reference data", planner.queries[-1])
        calls = [r["params"] for r in server.requests if r["method"] == "tools/call"]
        self.assertEqual([c["name"] for c in calls], ["web_search", "web_fetch"])
        self.assertEqual(calls[1]["arguments"]["urls"], [SOURCE_URL])
        self.assertEqual(calls[0]["arguments"]["session_id"], calls[1]["arguments"]["session_id"])
        self.assertEqual(calls[0]["arguments"]["model_name"], "gpt-4o")
        self.assertNotIn("private clipboard text", json.dumps(server.requests))
        self.assertNotIn("must-not-send", json.dumps(server.requests))
        self.assertTrue(all(r.closed for r in server.responses))

    def test_sse_responses_use_same_caller(self):
        server = MCPServer(sse=True)
        agent, planner = self.agent([tool_plan(SEARCH), FINAL_PLAN])
        with patch("requests.Session", return_value=server):
            self.assertEqual(self.predict(agent)[1], ["computer.keyboard.press('escape')\n"])
        self.assertIn("Remove Keybinding", planner.queries[-1])

    def test_enabled_provider_does_not_contact_mcp_without_model_request(self):
        agent, _ = self.agent([FINAL_PLAN])
        with patch("requests.Session") as session:
            self.predict(agent)
            session.assert_not_called()

    def test_saved_disable_and_explicit_override(self):
        with patch.dict(os.environ, {"WAA_SEARCH_PROVIDER": "none"}):
            agent, planner = self.agent([FINAL_PLAN])
            with patch("requests.Session") as session:
                self.predict(agent)
                session.assert_not_called()
            self.assertEqual(agent.search_provider, "none")
            self.assertNotIn("```web_tool", planner.system_prompt)
            override, _ = self.agent([FINAL_PLAN], "parallel")
            self.assertEqual(override.search_provider, "parallel")
        with patch.dict(os.environ, {"WAA_SEARCH_PROVIDER": "parallel"}):
            disabled, _ = self.agent([FINAL_PLAN], "none")
            self.assertIsNone(disabled.web_search)
        for value in ("", "other", False):
            with self.assertRaises(ValueError):
                resolve_search_provider(value)

    def test_errors_and_timeouts_are_consumed_without_retry(self):
        faults = [requests.Timeout(), requests.ConnectionError(),
                  {"isError": True, "content": [{"type": "text", "text": "quota exceeded"}]}]
        for fault in faults:
            with self.subTest(fault=fault):
                server = MCPServer(fault=fault)
                agent, planner = self.agent([tool_plan(SEARCH), FINAL_PLAN])
                with patch("requests.Session", return_value=server):
                    _, actions, logs, _ = self.predict(agent)
                self.assertEqual(actions, ["computer.keyboard.press('escape')\n"])
                self.assertIn("Web assistance failed", planner.queries[-1])
                self.assertIn("error", logs["web_tools"][0])
                self.assertEqual(sum(r["method"] == "tools/call" for r in server.requests), 1)

    def test_cancellation_propagates_without_another_model_or_tool_call(self):
        server = MCPServer(fault=KeyboardInterrupt())
        agent, planner = self.agent([tool_plan(SEARCH), FINAL_PLAN])
        with patch("requests.Session", return_value=server), self.assertRaises(KeyboardInterrupt):
            self.predict(agent)
        self.assertEqual(len(planner.queries), 1)

    def test_cancellation_while_reading_closes_response(self):
        response = Reply()
        def interrupted_read(**kwargs):
            raise KeyboardInterrupt()
        response.iter_content = interrupted_read
        server = MCPServer()
        server.post = lambda *args, **kwargs: response
        agent, planner = self.agent([tool_plan(SEARCH), FINAL_PLAN])
        with patch("requests.Session", return_value=server), self.assertRaises(KeyboardInterrupt):
            self.predict(agent)
        self.assertTrue(response.closed)
        self.assertEqual(len(planner.queries), 1)

    def test_budget_never_returns_tool_request_as_vm_code(self):
        server = MCPServer()
        agent, _ = self.agent([tool_plan(SEARCH)] * 3)
        with patch("requests.Session", return_value=server):
            _, actions, logs, _ = self.predict(agent)
        self.assertEqual(actions, ["WAIT"])
        self.assertEqual(sum(r["method"] == "tools/call" for r in server.requests), 2)
        self.assertIn("budget", logs["web_tools"][-1]["error"])

    def test_invalid_requests_cannot_send_data_or_execute_accompanying_code(self):
        invalid = [{"name": "delete_file", "arguments": {}},
                   {"name": "web_fetch", "arguments": {"urls": ["file:///etc/passwd"]}},
                   {"name": "web_fetch", "arguments": {"urls": ["http://127.0.0.1/private"]}},
                   {"name": "web_fetch", "arguments": {"urls": ["https://user:secret@example.com/"]}},
                   {"name": "web_search", "arguments": {"objective": "help", "search_queries": []}}]
        for request in invalid:
            with self.subTest(request=request):
                agent, _ = self.agent([tool_plan(request) + "\n```python\nraise Exception()\n```", FINAL_PLAN])
                with patch("requests.Session") as session:
                    self.assertEqual(self.predict(agent)[1], ["computer.keyboard.press('escape')\n"])
                    session.assert_not_called()

    def test_reset_closes_session_and_keeps_provider_choice(self):
        server = MCPServer()
        agent, _ = self.agent([tool_plan(SEARCH), FINAL_PLAN])
        with patch("requests.Session", return_value=server):
            self.predict(agent)
        old_session_id = agent.web_search.session_id
        agent.reset()
        self.assertTrue(server.closed)
        self.assertNotEqual(old_session_id, agent.web_search.session_id)
        self.assertEqual(agent.search_provider, "parallel")

    def test_ambient_netrc_is_not_used_by_real_request_preparation(self):
        # Exercise requests itself: an ambient login must not become Authorization.
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "netrc")
            with open(path, "w") as f:
                f.write("machine search.parallel.ai login unwanted password secret\n")
            client = ParallelSearchClient("gpt-4o")
            headers = []

            def send(session, request, **kwargs):
                headers.append(dict(request.headers))
                raise requests.Timeout()

            with patch.dict(os.environ, {"NETRC": path}), patch.object(requests.Session, "send", send):
                with self.assertRaises(SearchError):
                    client.call(**SEARCH)
            self.assertNotIn("Authorization", headers[0])
            self.assertEqual(headers[0]["User-Agent"], USER_AGENT)
            client.reset()

    def test_malformed_identity_redirect_and_oversized_response_are_errors(self):
        responses = [Reply({"jsonrpc": "2.0", "id": 99, "result": {}}),
                     Reply(status=302), Reply(raw=b"not json"),
                     Reply(raw=b"x" * (MAX_RESPONSE_BYTES + 1))]
        for response in responses:
            with self.subTest(response=response):
                server = MCPServer()
                server.post = lambda *args, **kwargs: response
                client = ParallelSearchClient("gpt-4o")
                with patch("requests.Session", return_value=server), self.assertRaises(SearchError):
                    client.call(**SEARCH)
                self.assertTrue(response.closed)

    def test_unadvertised_or_malformed_tool_schema_never_invokes_tool(self):
        for schema in (None, {}, {"type": "object", "required": [None]},
                       {"type": "object", "required": ["new_unsupported_field"]}):
            with self.subTest(schema=schema):
                client = ParallelSearchClient("gpt-4o")
                client.tools = {} if schema is None else {"web_search": schema}
                with patch("requests.Session") as session:
                    with self.assertRaises(SearchError):
                        client.call(**SEARCH)
                    session.assert_not_called()


if __name__ == "__main__":
    unittest.main()
