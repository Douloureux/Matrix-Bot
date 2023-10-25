from subprocess import check_output, call
from commands import docs
import json
import random
from uptime import uptime

def get_temperature() -> str:
    temp = check_output("vcgencmd measure_temp", shell=True).decode('ascii').strip().replace("temp=", "")
    return temp

def sys_upgrade() -> str:
    call([
        'sudo',
        'apt-get',
        'upgrade',
        '-y'
    ])

def shell(cmd) -> str:
    return check_output(cmd, shell=True).decode('ascii').strip()

def get_chromium() -> str:
    latest_version = check_output(
            """curl -s https://omahaproxy.appspot.com/all?csv=1 | grep win,stable | awk -F"," '{print $3}'"""
        , shell=True).decode('ascii').strip()
    return latest_version

def get_owner() -> str:
    return json.load(open(".env"))["owner_username"]

def get_username() -> str:
    return json.load(open(".env"))["username"]

def get_password() -> str:
    return json.load(open(".env"))["password"]

def get_homeserver() -> str:
    return json.load(open(".env"))["homeserver"]

def get_uptime() -> str:
    up = uptime()
    parts = []

    days, up = up // 86400, up % 86400
    if days:
        parts.append('%d day%s' % (days, 's' if days != 1 else ''))

    hours, up = up // 3600, up % 3600
    if hours:
        parts.append('%d hour%s' % (hours, 's' if hours != 1 else ''))

    minutes, up = up // 60, up % 60
    if minutes:
        parts.append('%d minute%s' % (minutes, 's' if minutes != 1 else ''))

    return 'Uptime: %s' % ', '.join(parts)

def rate() -> int:
    return random.randint(0, 100)

def send_help(input) -> str:    
    if (input is None) or (input not in docs.commands):
        return docs.help
    i = 0
    try:
        for j in docs.commands:
            if j == input:
                break
            else:
                i += 1
        return docs.help_text[i]
    except IndexError:
        return docs.help
    
def send_dev_help() -> str:
    return docs.dev_help
    
def privacy_filter(message: str) -> str:
    def link_finder(message: str) -> list:
        words = message.split()
        links = []
        for i in words:
            if "https://" in i:
                links.append(i)
        return links

    def tracker_remover(link: str) -> str:
        if "youtu.be" in link or "youtube.com" in link:
            return link
        else:
            a = link.split('?')
            return a[0]

    def replacer(link: str) -> str:
        return link.replace('www.reddit.com', 'libredd.it'
                    ).replace('twitter.com', 'nitter.net'
                    ).replace('www.youtube.com', 'yewtu.be'
                    ).replace('youtu.be', 'yewtu.be'
                    ).replace('m.youtube.com', 'yewtu.be'
                    ).replace('youtube.com', 'yewtu.be')
    
    def required(originalList: list, finalList: list) -> bool:
        print(originalList)
        print(finalList)
        if len(originalList) == 1:
            if originalList[0] == finalList[0]:
                return False
            else: 
                return True
        else:
            return True
    original = link_finder(message)
    linkList = link_finder(message)

    i = 0
    while i < len(linkList):
        linkList[i] = replacer(tracker_remover(linkList[i]))
        i += 1

    if required(original, linkList):
        return linkList[0]
    
    else:
        returnList = []
        i = 0
        while i < len(linkList):
            returnList.append(f"Link {i + 1}: {linkList[i]}")
        return '\n'.join(returnList)
