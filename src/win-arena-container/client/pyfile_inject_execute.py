
import os
import os.path
import logging
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from desktop_env.controllers.python import PythonController
from desktop_env.envs.desktop_env import DesktopEnv


logger = logging.getLogger("inject_and_execute")

def inject_and_execute(envV: DesktopEnv, controllerV: PythonController):
    print("1")
    # prepare basic infos
    pyFile = "hello_world.py"
    local_path: str = "./"+pyFile
    path: str = "C:/Users/Docker/Desktop/" + pyFile
    # action = "python "+path
    # has terminal window overlap
    # action = "import subprocess; subprocess.Popen('python "+path+"',creationflags=subprocess.CREATE_NEW_CONSOLE);"
    # no terminal window overlap
    action = "import subprocess; subprocess.Popen('pythonw "+path+"',creationflags=subprocess.CREATE_NEW_CONSOLE);"

    # inject execute py file through upload post request
    if not os.path.exists(local_path):
        print(f"Setup Upload - Invalid local path ({local_path}).")
        return

    print("2")
    form = MultipartEncoder({
        "file_path": path,
        "file_data": (os.path.basename(path), open(local_path, "rb"))
    })
    headers = {"Content-Type": form.content_type}
    print(form.content_type)

    ## send request to server to upload file
    http_server = f"http://{controllerV.vm_ip}:5000"
    
    logger.info("upload py file 4 injection: "+str(form))
    
    print("3")
    try:
        print("REQUEST ADDRESS: %s", http_server + "/setup" + "/upload")
        print("REQUEST FORM: "+str(form))
        response = requests.post(http_server + "/setup" + "/upload", headers=headers, data=form)
        if response.status_code == 200:
            print("Command executed successfully: " + response.text)
        else:
            print("Failed to upload file. Status code: " + response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred while trying to send the request: " + e)

    # execute py file through execute_python_windows_command post request
    print("4")
    print("controllerV.execute_python_windows_command: "+str(action))
    controllerV.execute_python_command(action)
    # controllerV.execute_command_new_terminal(action)
    print("5")


def notify(envV: DesktopEnv, controllerV: PythonController, data: str):
    # prepare basic infos
    pyFile = "hello_world.py"
    local_path: str = "./"+pyFile
    path: str = "C:/Users/Docker/Desktop/" + pyFile
    http_server = f"http://{controllerV.vm_ip}:5000"

    
    form = MultipartEncoder({
        "file_path": path,
        "file_data": data
    })
    headers = {"Content-Type": form.content_type}

    try:
        print("REQUEST ADDRESS: %s", http_server + "/notify")
        print("REQUEST FORM: "+str(form))
        response = requests.post(http_server + "/notify", headers=headers, data=form)
        if response.status_code == 200:
            print("Command executed successfully: " + response.text)
        else:
            print("Failed to upload file. Status code: " + response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred while trying to send the request: " + e)

