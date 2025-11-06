from ..constants import SETTINGS_PATH
import json
import subprocess

def load_settings():
    try:
      with open(SETTINGS_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Settings file not found. Please run the setup process.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from settings file. Maybe you changed it manually?")

def call_agent(question:str, screenshot:str, model:str="claude-sonnet-4.5"):
    settings = load_settings()
    command = f"{settings.get('cli')} "
    match settings['cli']:
        case "codex":
            command += "exec --full-auto "
            if screenshot:
                command += f"-i {screenshot}"
        case "copilot":
            command += "-p --allow-tools "
            question +=f"Before doing anything, analyze the image available at {screenshot}"
        case "claude":
            command += '-p --allowedTools "Bash,Read" --permission-mode acceptEdits'
            if screenshot:
                command += f" -i {screenshot}"
    process = subprocess.Popen(command.split() + [question], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        raise RuntimeError(f"Agent command failed: {error.decode().strip()}")
    return output.decode().strip()

