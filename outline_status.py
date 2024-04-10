import subprocess
import json


def find_outline_intf():
    command = "ip a"
    result = subprocess.run(command.split(), capture_output=True, text=True)

    return "outline233" in result.stdout


def print_outline_status():
    data = {}
    if find_outline_intf():
        data['text'] = " "
        print(json.dumps(data))
    else:
        data['text'] = " "
        print(json.dumps(data))


if __name__ == "__main__":
    print_outline_status()
