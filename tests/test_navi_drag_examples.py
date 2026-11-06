"""Execute Navi's drag examples without importing the GUI server or moving a mouse."""

import ast
from pathlib import Path
import runpy
from types import SimpleNamespace
import unittest
from unittest.mock import Mock


ROOT = Path(__file__).resolve().parents[1] / "src" / "win-arena-container"


class TestNaviDragExamples(unittest.TestCase):
    def test_prompt_drag_examples_match_server_api(self):
        server_path = ROOT / "vm" / "setup" / "server" / "computer.py"
        server_ast = ast.parse(server_path.read_text(encoding="utf-8"))
        mouse_class = next(
            node
            for node in server_ast.body
            if isinstance(node, ast.ClassDef) and node.name == "Mouse"
        )
        # Importing computer.py initializes Win32 input devices. Compile its real
        # Mouse class in isolation so these examples can run safely on any host.
        namespace = {"pyautogui": Mock(), "time": Mock(), "sleep_after_execution": 0.25}
        exec(
            compile(ast.Module(body=[mouse_class], type_ignores=[]), str(server_path), "exec"),
            namespace,
        )
        mouse = namespace["Mouse"]([], (0, 0, 1920, 1080), logger=Mock())
        prompts = runpy.run_path(
            str(ROOT / "client" / "mm_agents" / "navi" / "gpt" / "planner_messages.py")
        )

        for name in ("planning_system_message", "planning_system_message_shortened_previmg"):
            with self.subTest(prompt=name):
                examples = [
                    line
                    for line in prompts[name].splitlines()
                    if line.startswith("computer.mouse.drag(")
                ]
                self.assertEqual(len(examples), 1)
                namespace["pyautogui"].reset_mock()
                exec(examples[0], {"computer": SimpleNamespace(mouse=mouse)})
                namespace["pyautogui"].dragTo.assert_called_once_with(
                    640, 360, button="left"
                )


if __name__ == "__main__":
    unittest.main()
