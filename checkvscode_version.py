import subprocess

def get_vscode_version():
    try:
        # Execute the command to get VSCode version
        result = subprocess.run(["code", "--version"], capture_output=True, text=True)
        # Check if the command was successful
        if result.returncode == 0:
            print("VSCode Version:\n" + result.stdout)
        else:
            print("Could not determine VSCode version. Make sure 'code' command is available.")
    except FileNotFoundError:
        print("VSCode command-line tools are not installed or 'code' command is not available in PATH.")

get_vscode_version()
