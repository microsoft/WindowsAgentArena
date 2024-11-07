"""Script to run end-to-end evaluation on the benchmark.
Utils and basic architecture credit to https://github.com/web-arena-x/webarena/blob/main/run.py.
"""
import argparse
import datetime
import json
import logging
import os
import random
import sys
import shutil
import traceback
# import wandb

from tqdm import tqdm

import lib_run_single
from desktop_env.envs.desktop_env import DesktopEnv
from mm_agents.navi.agent import NaviAgent
import requests
import time

from threading import Event
import signal


print("Waiting for the server to start...")

#  Logger Configs {{{ #
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.propagate = True
datetime_str: str = datetime.datetime.now().strftime("%Y%m%d@%H%M%S")
formatter = logging.Formatter(
    fmt="\x1b[1;33m[%(asctime)s \x1b[31m%(levelname)s \x1b[32m%(module)s/%(lineno)d-%(processName)s\x1b[1;33m] \x1b[0m%(message)s")
def setup_logging(args):
    logging_dir: str = os.path.join(
        args.result_dir, 
        "logs"
    )
    
    os.makedirs(logging_dir, exist_ok=True)

    file_handler = logging.FileHandler(os.path.join(logging_dir, "normal-{}-{}.log".format(args.worker_id, datetime_str)), encoding="utf-8")
    debug_handler = logging.FileHandler(os.path.join(logging_dir, "debug-{}-{}.log".format(args.worker_id, datetime_str)), encoding="utf-8")
    stdout_handler = logging.StreamHandler(sys.stdout)
    sdebug_handler = logging.FileHandler(os.path.join(logging_dir, "sdebug-{}-{}.log".format(args.worker_id, datetime_str)), encoding="utf-8")

    file_handler.setLevel(logging.INFO)
    debug_handler.setLevel(logging.DEBUG)
    stdout_handler.setLevel(logging.INFO)
    sdebug_handler.setLevel(logging.DEBUG)

    file_handler.setFormatter(formatter)
    debug_handler.setFormatter(formatter)
    stdout_handler.setFormatter(formatter)
    sdebug_handler.setFormatter(formatter)

    stdout_handler.addFilter(logging.Filter("desktopenv"))
    sdebug_handler.addFilter(logging.Filter("desktopenv"))

    root_logger.addHandler(file_handler)
    root_logger.addHandler(debug_handler)
    root_logger.addHandler(stdout_handler)
    root_logger.addHandler(sdebug_handler)
#  }}} Logger Configs # 

logger = logging.getLogger("desktopenv.experiment")

def config() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run end-to-end evaluation on the benchmark"
    )

    # environment config
    parser.add_argument(
        "--headless", action="store_true", help="Run in headless machine"
    )
    parser.add_argument("--action_space", type=str, default="pyautogui", help="Action type")
    parser.add_argument(
        "--observation_type",
        choices=[
            "screenshot",
            "a11y_tree",
            "screenshot_a11y_tree",
            "som"
        ],
        default="a11y_tree",
        help="Observation type",
    )
    parser.add_argument("--screen_width", type=int, default=1920)
    parser.add_argument("--screen_height", type=int, default=1200)
    parser.add_argument("--sleep_after_execution", type=float, default=3)
    parser.add_argument("--max_steps", type=int, default=15)
    parser.add_argument("--a11y_backend", type=str, default="uia") # "uia" or "win32"

    # agent config
    parser.add_argument("--agent_name", type=str, default="navi")
    parser.add_argument("--som_origin", type=str, default="oss") # options: 'oss', 'a11y', 'mixed-oss'
    parser.add_argument("--max_trajectory_length", type=int, default=3)
    parser.add_argument("--test_config_base_dir", type=str, default="evaluation_examples_windows")

    # lm config
    parser.add_argument("--model", type=str, default="gpt-4-vision-preview") #gpt-4o-mini or gpt-4-vision-preview or gpt-4o or gpt-4-1106-vision-preview
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--top_p", type=float, default=0.9)
    parser.add_argument("--max_tokens", type=int, default=1500)
    parser.add_argument("--stop_token", type=str, default=None)

    # example config
    parser.add_argument("--domain", type=str, default="all")
    parser.add_argument("--emulator_ip", type=str, default="20.20.20.21")

    parser.add_argument("--test_all_meta_path", type=str, default="evaluation_examples_windows/test_all.json") # or test_custom.json for a single task

    # logging related
    parser.add_argument("--result_dir", type=str, default="./results")
    parser.add_argument("--trial_id", type=str, default="0")

    # multi-worker related
    parser.add_argument("--worker_id", type=int, default=0, help="ID of the worker")  
    parser.add_argument("--num_workers", type=int,  default=1, help="Total number of workers") 

    # benchmark difficulty level
    parser.add_argument("--diff_lvl", type=str, default="normal", help="Difficulty level of the benchmark")  

    args, unknownargs = parser.parse_known_args()

    return args

def test(
        args: argparse.Namespace,
        test_all_meta: dict
) -> None:
    scores = []
    max_steps = args.max_steps

    # log args
    logger.info("Args: %s", args)
    # set wandb project
    cfg_args = \
    {
        "headless": args.headless,
        "action_space": args.action_space,
        "observation_type": args.observation_type,
        "screen_width": args.screen_width,
        "screen_height": args.screen_height,
        "sleep_after_execution": args.sleep_after_execution,
        "max_steps": args.max_steps,
        "a11y_backend": args.a11y_backend,
        "max_trajectory_length": args.max_trajectory_length,
        "agent_name": args.agent_name,
        "som_origin": args.som_origin,
        "model": args.model,
        "temperature": args.temperature,
        "top_p": args.top_p,
        "max_tokens": args.max_tokens,
        "stop_token": args.stop_token,
        "result_dir": args.result_dir,
        "trial_id": args.trial_id,
        "worker_id": args.worker_id,
        "num_workers": args.num_workers,
    }

    if cfg_args["agent_name"] == "navi":
        if cfg_args["som_origin"] in ["a11y", "omni", "mixed-omni"]:
            som_config = None
        elif cfg_args["som_origin"] in ["oss", "mixed-oss"]:
            som_config = {
                "pipeline": ["webparse", "groundingdino", "ocr"],
                "groundingdino": {
                    "prompts": ["icon", "image"]
                },
                "ocr": {
                    "class_name": "TesseractOCR"
                },
                "webparse": {
                    "cdp_url": f"http://{args.emulator_ip}:9222"
                }
            }
        
        agent = NaviAgent(
            server="oai",
            model=args.model,
            som_config=som_config,
            som_origin=args.som_origin,
            temperature=args.temperature
        )
    elif cfg_args["agent_name"] == "claude":
        from mm_agents.claude.agent import ClaudeAgent
        agent = ClaudeAgent()
    else:
        raise ValueError(f"Unknown agent name: {cfg_args['agent_name']}")
    
    env = DesktopEnv(
        action_space=agent.action_space,
        screen_size=(args.screen_width, args.screen_height),
        headless=args.headless,
        require_a11y_tree=args.observation_type in ["a11y_tree", "screenshot_a11y_tree", "som"],
        emulator_ip=args.emulator_ip, #for OS running on docker
        a11y_backend=args.a11y_backend
    )

    for domain in tqdm(test_all_meta, desc="Domain"):
        for example_id in tqdm(test_all_meta[domain], desc="Example", leave=False):
            
            if args.diff_lvl == "normal":
                logger.info(f"Windows Agent Arena: Starting on NORMAL difficulty")
                config_file = os.path.join(args.test_config_base_dir, f"examples/{domain}/{example_id}.json")
                logger.info(f"\nTESTING ON TASK CONFIG PATH: {config_file}")

            elif args.diff_lvl == "hard":
                logger.info(f"Windows Agent Arena: Starting on HARDER difficulty")
                
                config_file = os.path.join(args.test_config_base_dir, f"examples_noctxt/{domain}/{example_id}.json")
                logger.info(f"\nTESTING ON TASK CONFIG PATH: {config_file}")

            else:
                sys.exit("Invalid value for arg --diff_lvl. Choose 'normal' or 'hard'.")

            with open(config_file, "r", encoding="utf-8") as f:
                example = json.load(f)

            logger.info(f"[Domain]: {domain}")
            logger.info(f"[Example ID]: {example_id}")

            instruction = example["instruction"]

            logger.info(f"[Instruction]: {instruction}")
            # wandb each example config settings
            cfg_args["instruction"] = instruction
            cfg_args["start_time"] = datetime.datetime.now().strftime("%Y:%m:%d-%H:%M:%S")
            # run.config.update(cfg_args)

            example_result_dir = os.path.join(
                args.result_dir,
                args.action_space,
                args.observation_type,
                args.model,
                args.trial_id,
                domain,
                example_id
            )
            os.makedirs(example_result_dir, exist_ok=True)
            
            # Example Logging Config {{{
            os.makedirs(os.path.join(example_result_dir, "logs"), exist_ok=True)
            task_log_handler = logging.FileHandler(os.path.join(example_result_dir, "logs", "task-{}-{}.log".format(args.worker_id, datetime_str)), encoding="utf-8")
            task_log_handler.setLevel(logging.DEBUG)
            task_log_handler.setFormatter(formatter)
            root_logger.addHandler(task_log_handler)
            # }}} Example Logging Config
            
            # example start running
            try:
                lib_run_single.run_single_example(agent, env, example, max_steps, instruction, args, example_result_dir,
                                                  scores)
            except Exception as e:
                logger.error(f"Exception in {domain}/{example_id}: {e}")
                error_traceback = traceback.format_exc()
                logger.error(error_traceback)
                # env.controller.end_recording(os.path.join(example_result_dir, "recording.mp4"))
                # Write error details to traj.jsonl
                with open(os.path.join(example_result_dir, "traj.jsonl"), "a") as f:
                    f.write(json.dumps({
                        "Error": f"Exception in {domain}/{example_id}",
                        "Exception": str(e),
                        "Traceback": error_traceback,
                    }))
                    f.write("\n")
                
                # Write error details with stack trace to traj.html
                with open(os.path.join(example_result_dir, "traj.html"), "a") as f:
                    f.write(f"<h1>Error: Exception in {domain}/{example_id}</h1>")
                    f.write(f"<p>{e}</p>")
                    f.write("<pre>")
                    f.write(error_traceback)
                    f.write("</pre>")
            else:
                logger.info(f"Finished {domain}/{example_id}")
            finally:
                # Cleanup task log handler
                root_logger.removeHandler(task_log_handler)
                task_log_handler.close()

    env.close()
    # logger.info(f"UPDATED SCORES: {scores}")
        
    if len(scores) == 0:
        logger.info("No examples finished.")
    else:
        logger.info(f"Average score: {sum(scores) / len(scores)}")


def get_unfinished(action_space, use_model, observation_type, result_dir, trial_id, total_file_json):
    target_dir = os.path.join(result_dir, action_space, observation_type, use_model, trial_id)

    if not os.path.exists(target_dir):
        return total_file_json

    finished = {}
    for domain in os.listdir(target_dir):
        finished[domain] = []
        domain_path = os.path.join(target_dir, domain)
        if os.path.isdir(domain_path):
            for example_id in os.listdir(domain_path):
                if example_id == "onboard":
                    continue
                example_path = os.path.join(domain_path, example_id)
                if os.path.isdir(example_path):
                    if "result.txt" not in os.listdir(example_path):
                        # empty all files and dirs under example_id
                        for file in os.listdir(example_path):
                            out_path = os.path.join(example_path, file)
                            if os.path.isdir(out_path):
                                shutil.rmtree(out_path)
                            else:
                                os.remove(out_path)
                    else:
                        finished[domain].append(example_id)

    if not finished:
        return total_file_json

    for domain, examples in finished.items():
        if domain in total_file_json:
            total_file_json[domain] = [x for x in total_file_json[domain] if x not in examples]

    return total_file_json


def get_result(action_space, use_model, observation_type, result_dir, trial_id, total_file_json):
    target_dir = os.path.join(result_dir, action_space, observation_type, use_model, trial_id)
    if not os.path.exists(target_dir):
        print("New experiment, no result yet.")
        return None

    all_result = []

    for domain in os.listdir(target_dir):
        domain_path = os.path.join(target_dir, domain)
        if os.path.isdir(domain_path):
            for example_id in os.listdir(domain_path):
                example_path = os.path.join(domain_path, example_id)
                if os.path.isdir(example_path):
                    if "result.txt" in os.listdir(example_path):
                        # empty all files under example_id
                        try:
                            all_result.append(float(open(os.path.join(example_path, "result.txt"), "r").read()))
                        except:
                            all_result.append(0.0)

    if not all_result:
        print("New experiment, no result yet.")
        return None
    else:
        print("Current Success Rate:", sum(all_result) / len(all_result) * 100, "%")
        return all_result


exit_event = Event()
def quit(signo, _frame):
    print("Interrupted by %d, shutting down" % signo)
    exit_event.set()
    exit(0)

    
def wait_for_server(ip, port=5000):
    while not exit_event.is_set():
        try:
            response = requests.get("http://"+ip+":"+str(port)+"/probe", timeout=7)
            print("Response from server:", response.json())
            break  # If the request is successful, break the loop
        except Exception as e:
            print("Failed to get hello:", e)
            print("Retrying...")
            exit_event.wait(5)  # Wait for 5 seconds before retrying

# Handling keyboard interrupts
for sig in ('TERM', 'HUP', 'INT'):
    signal.signal(getattr(signal, 'SIG'+sig), quit)

if __name__ == '__main__':
    ####### The complete version of the list of examples #######
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    args = config()
    setup_logging(args)

    wait_for_server(args.emulator_ip)

    with open(args.test_all_meta_path, "r", encoding="utf-8") as f:
        test_all_meta = json.load(f)

    logger.info(f"\nTESTING ON TASK JSON PATH: {args.test_all_meta_path}")

    if args.domain != "all":
        test_all_meta = {args.domain: test_all_meta[args.domain]}
    
    if args.num_workers == 1:
        test_file_list = get_unfinished(
            args.action_space,
            args.model,
            args.observation_type,
            args.result_dir,
            args.trial_id,
            test_all_meta
        )
    else:
        # if we have more than one worker (Azure runs) then we distribute the tasks equally
        # otherwise they will try to delete each other's partial results in get_unfinished
        test_file_list = test_all_meta

    left_info = ""
    for domain in test_file_list:
        left_info += f"{domain}: {len(test_file_list[domain])}\n"
    logger.info(f"Left tasks:\n{left_info}")

    # distribute tasks among workers
        # Flatten your dict into a list of tasks  
    all_tasks_test  = [(domain, example_id) for domain in test_file_list for example_id in test_file_list[domain]]  

    # Calculate the start and end indices of the tasks for this worker    
    tasks_per_worker = len(all_tasks_test) // args.num_workers    
    extra = len(all_tasks_test) % args.num_workers  # calculate the number of tasks that can't be evenly distributed  
    
    start_index = args.worker_id * tasks_per_worker + min(args.worker_id, extra)  
    if args.worker_id < extra:  
        end_index = start_index + tasks_per_worker + 1  
    else:  
        end_index = start_index + tasks_per_worker  
    
    # Slice the tasks for this worker  
    tasks_for_this_worker = all_tasks_test[start_index:end_index]

    # log which tasks this worker is doing
    logger.info(f"Worker {args.worker_id} is doing tasks: {tasks_for_this_worker}")
  
    # Convert the list of tasks back to a dictionary  
    test_file_list_worker = {}  
    for domain, example_id in tasks_for_this_worker:  
        if domain not in test_file_list_worker: 
            # create an empty list to which elements will be appended 
            test_file_list_worker[domain] = []  
        test_file_list_worker[domain].append(example_id)  

    get_result(args.action_space,
        args.model,
        args.observation_type,
        args.result_dir,
        args.trial_id,
        test_file_list_worker
    )
    test(args, test_file_list_worker)
