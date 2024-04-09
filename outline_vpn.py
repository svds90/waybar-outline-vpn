import subprocess
import psutil
import sys
import os

import json
from pprint import pprint


outline_cli_command = ("sudo go run github.com/Jigsaw-Code/outline-sdk/x/examples"
                       "/outline-cli@latest -transport")

outline_command = f"{outline_cli_command} {outline_key}"

outline_processes = []


def find_outline_procs():
    global outline_processes

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if "outline-cli" in proc.info['name'] and proc.info['username'] == 'root':
            outline_processes.append(proc)


def outline_status():
    find_outline_procs()
    return bool(outline_processes)


def outline_run(command):
    process = subprocess.Popen(
        command.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    for line in process.stdout:  # type: ignore
        print(line, end="")

    for line in process.stderr:  # type: ignore
        print(line, end="")


def outline_stop():
    if outline_processes:
        for proc in outline_processes:
            os.system(f"sudo kill -SIGTERM {proc.pid}")

            try:
                proc.wait(timeout=1)
            except psutil.TimeoutExpired:
                os.system(f"sudo kill -SIGKILL {proc.pid}")


def outline_toggle():
    if outline_status() is True:
        outline_stop()
    else:
        outline_run(outline_command)


if __name__ == "__main__":
    data = {}
    if len(sys.argv) > 1 and sys.argv[1] == "status":
        if outline_status():
            data['text'] = "󱇱 "
            print(json.dumps(data), flush=True)
        else:
            data['text'] = "󰅤 "
            print(json.dumps(data), flush=True)

    elif len(sys.argv) > 1 and sys.argv[1] == "toggle":
        data['text'] = "123"
        print(json.dumps(data))
        outline_toggle()
