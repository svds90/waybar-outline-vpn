import threading
import subprocess
import psutil
import os
import json

outline_key = ""

outline_cli_dir = ""

outline_command = f"sudo {outline_cli_dir} -transport {outline_key}"

outline_processes = []


def find_outline_procs():
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


def send_waybar_signal():
    os.system("pkill -RTMIN+8 waybar")


def outline_toggle():
    if outline_status() is True:
        outline_stop()
        send_waybar_signal()
    else:
        toggle_thread = threading.Thread(target=outline_run, args=(outline_command,))
        toggle_thread.start()
        send_waybar_signal()


if __name__ == "__main__":
    outline_toggle()
