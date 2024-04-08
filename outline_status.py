import subprocess
import json


def find_outline_interface():
    command = "ip a"
    data = {}
    result = subprocess.run(command.split(), capture_output=True, text=True)

    if "outline233" in result.stdout:
        data['text'] = " "
        print(json.dumps(data))
    else:
        data['text'] = " "
        print(json.dumps(data))


if __name__ == "__main__":
    find_outline_interface()
