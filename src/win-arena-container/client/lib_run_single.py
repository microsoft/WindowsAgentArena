import datetime
import json
import logging
import os
import pickle
import numpy as np
import html as html_lib
from wrapt_timeout_decorator import *
import time
import traceback


logger = logging.getLogger("desktopenv.experiment")

# Open the JSON file
with open("./settings.json", "r") as file:
    # Load the JSON data from the file
    data = json.load(file)
time_limit = data["time_limit"]

def save_dict(info_dict, path, step_idx, action_timestamp) -> dict:
    """
    Save each key of the observation to the specified path. parsing the correct datatypes.
    """
    file_format = "{key}-step_{step_idx}_{action_timestamp}.{ext}"
    obs_content = {k:None for k in info_dict.keys()}
    for key, value in info_dict.items():
        file_path = None
        #accessibility tree in a txt file
        if key == "accessibility_tree" or key == "user_question" or key == "plan_result":
            file_path = os.path.join(path, file_format.format(key=key, step_idx=step_idx, action_timestamp=action_timestamp, ext="txt"))
            if value:
                with open(file_path, "w") as f:
                    f.write(value)
            else:
                with open(file_path, "w") as f:
                    f.write("No data available")
            obs_content[key] = file_path
        # image, in bytes
        elif isinstance(value, bytes):
            file_path = os.path.join(path, file_format.format(key=key, step_idx=step_idx, action_timestamp=action_timestamp, ext="png"))
            with open(file_path, "wb") as f:
                f.write(value)
            obs_content[key] = file_path
        # number
        elif isinstance(value, (int, float)):
            # do not save a unique file just for a scalar
            obs_content[key] = value
        # vectors
        elif isinstance(value, (list, tuple, np.ndarray)) and len(value) > 0 and isinstance(value[0], (int, float)):
            obs_content[key] = value
        # text
        elif isinstance(value, str):
            obs_content[key] = value
        # npy file
        elif isinstance(value, np.ndarray):
            file_path = os.path.join(path, file_format.format(key=key, step_idx=step_idx, action_timestamp=action_timestamp, ext="npy"))
            np.save(file_path, value)
            obs_content[key] = file_path
        # PIL image
        elif "PIL" in str(type(value)):
            file_path = os.path.join(path, file_format.format(key=key, step_idx=step_idx, action_timestamp=action_timestamp, ext="png"))
            value.save(file_path)
            obs_content[key] = file_path
        # dict
        elif isinstance(value, dict):
            file_path = os.path.join(path, file_format.format(key=key, step_idx=step_idx, action_timestamp=action_timestamp, ext="json"))
            with open(file_path, "w") as f:
                f.write(json.dumps(value))
            obs_content[key] = file_path
        # list
        elif isinstance(value, list):
            file_path = os.path.join(path, file_format.format(key=key, step_idx=step_idx, action_timestamp=action_timestamp, ext="json"))
            with open(file_path, "w") as f:
                f.write(json.dumps(value))
            obs_content[key] = file_path
        else:
            obs_content[key] = f"key: {key}: "+str(type(value))+" not saved"
    return obs_content

# dict -> html
def dict_to_html(in_dict, name):
    html = []
    def append_kv(key, value):
        ext = "txt" if not isinstance(value, str) else value.split(".")[-1]
        if ext not in ["png", "jpg", "jpeg", "txt"]:
            ext = "txt"
        value = str(value)
        is_path = '/' in value
        
        # display prompts
        if key == "user_question" or key == "plan_result":
            is_path = False
            # value = logs.get(key, value)
        
        # use <details> for a collapsible section
        html.append("<details>")
        html.append(f"<summary>{key}</summary>")
        if is_path: # link files
            html.append(f"<a href='{os.path.basename(value)}'>")
        if ext in ["png", "jpg", "jpeg"]: # display images
            html.append(f"<img style='max-width: 100%' src='{os.path.basename(value)}'/>")
        elif ext in ["txt"]: # display text
            html.append(f"<pre>\n{html_lib.escape(value)}\n</pre>")
        if is_path:
            html.append("</a>")
        html.append("</details>")
    html.append("<details>")
    html.append(f"<summary>{html_lib.escape(name)}</summary>")
    for key, value in in_dict.items():
        append_kv(key, value)
    html.append("</details>")
    return html
    

def start_html(
    example,
    example_result_dir,
    init_dict
):
    html = []
    
    # dump config, theme, instruction
    html += [
        "<style>",
        # minimal styling {{{
        "html { font-family: sans-serif; } ",
        "summary { cursor: text; } ",
        "details details>summary { padding-left: 0.5em; } ",
        "#theme-selector { float: right; text-align: center; opacity: 0.5; } ",
        # }}} minimal styling
        # light theme {{{
        ":root {",
        "    --background-color: #ffffff;",
        "    --text-color: #000000;",
        "    --summary-hover: #f0f0f0;",
        "    --summary-open: #ececec;",
        "    --link-color: #1e90ff;",
        "    --link-hover-color: #104e8b;",
        "}",
        # }}} light theme
        
        # eyeballed this to look good w/ vscode + nicer high contrast + live preview 
        # dark theme {{{
        "[data-theme='dark'] {",
        "    --background-color: #000000;",
        "    --text-color: #d4d4d4;",
        "    --summary-hover: #1e1e1e;",
        "    --summary-open: #1e1e1e;",
        "    --link-color: #1e90ff;",
        "    --link-hover-color: #63a4ff;",
        "}",
        # }}} dark theme
        
        # apply theme colors {{{
        "html, select {",
        "    background: var(--background-color);",
        "    color: var(--text-color);",
        "}",
        "summary:hover { background: var(--summary-hover); }",
        "details[open] > summary { background: var(--summary-open); }",
        "a { color: var(--link-color); }",
        "a:hover { color: var(--link-hover-color); }",
        "select { border: 1px solid var(--text-color); }",
        # }}} apply theme colors
        "</style>",
        # config, theme {{{
        "<details>",
        "<summary>config",
        # theme selector {{{
        "<select id='theme-selector' onchange='setTheme(this.value)'>",
        "  <option value='' disabled selected>Theme</option>",
        "  <option value='auto'>auto</option>",
        "  <option value='light'>light</option>",
        "  <option value='dark'>dark</option>",
        "</select>",
        "<script>",
        "function setTheme(theme) { if (theme === 'auto') { document.documentElement.removeAttribute('data-theme'); } else { document.documentElement.setAttribute('data-theme', theme); } }",
        "(function() { const theme = localStorage.getItem('theme') || 'auto'; document.getElementById('theme-selector').value = theme; setTheme(theme); document.getElementById('theme-selector').addEventListener('change', function() { localStorage.setItem('theme', this.value); }); })();",
        "</script>",
        # }}} theme selector
        "</summary>",
        f"<pre>\n{json.dumps(example, indent=2)}\n</pre>",
        "</details>",
        # }}} config, theme
    ]
    html.append(f"<pre>\n{example['instruction']}\n</pre>")
    
    # dump observation dict
    html += dict_to_html(init_dict, "env.reset(config)")
    obs_image = os.path.relpath(init_dict.get('screenshot'), example_result_dir)
    html.append(f"<img style='max-width: 100%' onclick='window.open(this.src, \"_blank\")' src='{obs_image}'/>")
    
    return "".join(html)

def save_html(
    example,
    obs_saved_content,
    logs_saved_content,
    example_result_dir,
    step_idx,
    action,
    logs,
    action_timestamp
):
    html = []
    
    # dump id and total elapsed time for that step
    html.append(f"<h3>Step {step_idx + 1} ({action_timestamp})</h3>")
    
    # dump response dict
    html += dict_to_html({
            **logs_saved_content, 
            'user_question': logs.get('user_question'), 
            'plan_result': logs.get('plan_result')
        }, "agent.predict(obs)")
    html.append(f"<pre>\n{html_lib.escape(action)}\n</pre>")
    
    # dump observation dict
    html += dict_to_html(obs_saved_content, "env.step(action)")
    if obs_saved_content.get('screenshot'):
        obs_image = os.path.relpath(obs_saved_content.get('screenshot', ""), example_result_dir)
        html.append(f"<img style='max-width: 100%' onclick='window.open(this.src, \"_blank\")' src='{obs_image}'/>")
    
    # keep all the html on one line
    return "".join(html)

# @timeout(time_limit, use_signals=False)
def run_single_example(agent, env, example, max_steps, instruction, args, example_result_dir, scores):
    print("starting agent reset")
    agent.reset()
    print("reset agent done")
    print("starting env reset")
    obs = env.reset(task_config=example)
    print("reset env done")
    done = False
    # done = True
    step_idx = 0
    start_time = datetime.datetime.now()
    # print("starting env controller recording")
    #env.controller.start_recording()
    
    # log env reset
    init_timestamp = start_time.strftime("%Y%m%d@%H%M%S")
    init_dict = save_dict(obs, example_result_dir, 'reset', init_timestamp)
    with open(os.path.join(example_result_dir, "traj.jsonl"), "a") as f:
        traj_data = {
            "step_num": 0,
            "action_timestamp": init_timestamp,
            "action": None
        }
        traj_data.update(init_dict)
        f.write(json.dumps(traj_data))
        f.write("\n")
    with open(os.path.join(example_result_dir, "traj.html"), "a") as f:
        f.write(start_html(
            example=example,
            example_result_dir=example_result_dir,
            init_dict=init_dict
        ))
    
    while not done and step_idx < max_steps:

        if obs is None:
            logger.error("Observation is None. Waiting a little to do next step.")
            time.sleep(5)
            step_idx += 1
            continue

        print("starting agent predict")
        response, actions, logs, computer_update_args = agent.predict(
            instruction,
            obs
        )
        print("agent predict done")


        # update the computer object
        if computer_update_args:
            print("starting env controller update computer")
            env.controller.update_computer(**computer_update_args)
            print("env controller update computer done")
        else:
            print("No computer update args provided.")
            
        for action in actions:
            # Capture the timestamp before executing the action
            action_timestamp = datetime.datetime.now().strftime("%Y%m%d@%H%M%S")
            elapsed_timestamp = f"{datetime.datetime.now() - start_time}"
            logger.info("Step %d: %s", step_idx + 1, action)
            print("starting env step")
            obs, reward, done, info = env.step(action, args.sleep_after_execution)
            print("env step done")

            logger.info("Reward: %.2f", reward)
            logger.info("Done: %s", done)
            
            # save the step's observation as a dict
            if obs:
                obs_saved_content = save_dict(obs, example_result_dir, step_idx, action_timestamp)
            else:
                obs_saved_content = {}
            if logs:
                logs_saved_content = save_dict(logs, example_result_dir, step_idx, action_timestamp)
            else:
                logs_saved_content = {}
            with open(os.path.join(example_result_dir, "traj.jsonl"), "a") as f:
                traj_data = {
                    "step_num": step_idx + 1,
                    "action_timestamp": action_timestamp,
                    "action": action,
                    "reward": reward,
                    "done": done,
                    "info": info,
                    "screenshot_file": f"step_{step_idx + 1}_{action_timestamp}.png"
                }
                traj_data.update(obs_saved_content)
                traj_data.update(logs_saved_content)
                # print(traj_data["accessibility_tree"])
                f.write(json.dumps(traj_data))
                f.write("\n")
            
            with open(os.path.join(example_result_dir, "traj.html"), "a") as f:
                f.write(save_html(
                    example=example,
                    obs_saved_content=obs_saved_content,
                    logs_saved_content=logs_saved_content,
                    example_result_dir=example_result_dir,
                    step_idx=step_idx,
                    action=action, 
                    logs=logs,
                    action_timestamp=elapsed_timestamp
                ))

            if done:
                logger.info("The episode is done.")
                break
        step_idx += 1
    print("starting env evaluate")

    result = env.evaluate()
    print("env evaluate done")
    logger.info("Result: %.2f", result)
    scores.append(result)
    with open(os.path.join(example_result_dir, "result.txt"), "w", encoding="utf-8") as f:
        f.write(f"{result}\n")
    with open(os.path.join(example_result_dir, "traj.html"), "a") as f:
        elapsed_timestamp = f"{datetime.datetime.now() - start_time}"
        f.write(f"<h1>Result: {result}</h1>")
        f.write(f"<h1>Elapsed Time: {elapsed_timestamp}</h1>")
    # print("ending env controller recording")

    # try:
    #     result = env.evaluate() 
    #     logger.info("Result: %.2f", result)
    #     logger.info(f"SCORES BEFORE APPENDING: {scores}")
    #     scores.append(result)
    #     logger.info(f"SCORES AFTER APPENDING: {scores}")
    #     with open(os.path.join(example_result_dir, "result.txt"), "w", encoding="utf-8") as f:
    #         f.write(f"{result}\n")
    # except Exception as e:
    #     logger.error(f"Error during evaluation: {e}")


    # env.controller.end_recording(os.path.join(example_result_dir, "recording.mp4"))
    print("env controller end recording done")