from utils import *
import requests.exceptions

def sys_update_reporter() -> str:
    update_pkgs = dpkg.get_update_packages()

    if dpkg.check_update(update_pkgs):
        return dpkg.return_updates(update_pkgs)
    else:
        return "No system updates available"
    
def synapse_update_reporter() -> str:
    try:
        if updates.synapse_update_check():
            return updates.synapse_update_message()
        else:
            return "Synapse is up to date"
    except requests.exceptions.ConnectionError:
        return "Homeserver is turned off"

def schildi_update_reporter() -> bool:
    return updates.schildi_update_check()

def element_update_reporter() -> bool:
    return updates.element_update_check()

def powershell_update_reporter() -> bool:
    return updates.powershell_update_check()