import requests
import json
import subprocess

def matrix_version() -> str:
    r = requests.get(f"http://localhost:8008/_synapse/admin/v1/server_version").content.decode()
    return "v" + str(json.loads(r)["server_version"])

def schildi_version():
    return "v" + open("/home/user/schildichat/version").read().strip()

def element_version():
    return "v" + open("/home/user/element/version").read().strip()

def powershell_version():
    return "v" + subprocess.check_output("pwsh --version", shell=True).decode('ascii').strip().replace("PowerShell ", "")

def latest_tag(owner, repo) -> str:
    token = json.load(open(".env"))["github"]
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/releases/latest", headers=headers)
    info = json.loads(r.content.decode())
    return str(info["tag_name"])

def synapse_update_check():
    if latest_tag("matrix-org", "synapse") == matrix_version():
        return False
    else:
        return True

def schildi_update_check():
    if latest_tag("SchildiChat", "schildichat-desktop") == schildi_version():
        return False
    else:
        return True
    
def element_update_check():
    if latest_tag("vector-im", "element-web") == element_version():
        return False   
    else:
        return True
    
def powershell_update_check():
    if latest_tag("PowerShell", "PowerShell") == powershell_version():
        return False
    else:
        return True

def synapse_update_message():
    return (f"Synapse has an update available, to version {latest_tag('matrix-org','synapse')}.\n"
            f"[Release notes](https://github.com/matrix-org/synapse/releases/tag/{latest_tag('matrix-org', 'synapse')})")