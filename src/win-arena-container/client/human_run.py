import datetime
import json
import logging
import os
import sys
import time
import argparse
from desktop_env.envs.desktop_env import DesktopEnv

#  Logger Configs {{{ # 
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

datetime_str: str = datetime.datetime.now().strftime("%Y%m%d@%H%M%S")

file_handler = logging.FileHandler(os.path.join("logs", "normal-{:}.log".format(datetime_str)), encoding="utf-8")
debug_handler = logging.FileHandler(os.path.join("logs", "debug-{:}.log".format(datetime_str)), encoding="utf-8")
stdout_handler = logging.StreamHandler(sys.stdout)
sdebug_handler = logging.FileHandler(os.path.join("logs", "sdebug-{:}.log".format(datetime_str)), encoding="utf-8")

file_handler.setLevel(logging.INFO)
debug_handler.setLevel(logging.DEBUG)
stdout_handler.setLevel(logging.INFO)
sdebug_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    fmt="\x1b[1;33m[%(asctime)s \x1b[31m%(levelname)s \x1b[32m%(module)s/%(lineno)d-%(processName)s\x1b[1;33m] \x1b[0m%(message)s")
file_handler.setFormatter(formatter)
debug_handler.setFormatter(formatter)
stdout_handler.setFormatter(formatter)
sdebug_handler.setFormatter(formatter)

stdout_handler.addFilter(logging.Filter("desktopenv"))
sdebug_handler.addFilter(logging.Filter("desktopenv"))

logger.addHandler(file_handler)
logger.addHandler(debug_handler)
logger.addHandler(stdout_handler)
logger.addHandler(sdebug_handler)
#  }}} Logger Configs # 

logger = logging.getLogger("desktopenv.main")


def human_agent():
    """
    Runs the Gym environment with human input.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--example', type=str, help="Path to the example json file.")
    args = parser.parse_args(sys.argv[1:])

    example_path = args.example if args.example is not None and os.path.exists(args.example) else \
        'evaluation_examples_windows/examples/chrome/af630914-714e-4a24-a7bb-f9af687d3b91-wos.json'
    with open(example_path, "r", encoding="utf-8") as f:
        example = json.load(f)

    env = DesktopEnv(
        action_space="pyautogui",
        require_a11y_tree="a11y_tree",
        emulator_ip="20.20.20.21", #for OS running on docker
    )
        
    # reset the environment to certain snapshot
    observation = env.reset(task_config=example)
    done = False
    logger.info('\x1b[32m[TASK INSTRUCTION]: \x1b[32;3m%s\x1b[0m', example["instruction"])

    input("Press Enter to start human operation...")
    human_start_time = time.time()
    input("Press Enter to finish human operation.")
    print("Time elapsed of human operation: %.2f" % (time.time() - human_start_time))

    result = env.evaluate()
    logger.info("Result: %.2f", result)

    # env.close()
    logger.info("Environment closed.")


if __name__ == "__main__":
    human_agent()
