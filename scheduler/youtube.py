import os, sys
from lib import rss, matrix_commander
import subprocess

def write_file(path, content):
    file = open(path, "w")
    file.write(content)

def read_file(path) -> str:
    file = open(path).read()
    return str(file).strip()

def youtube():
    vpath = "../db/youtube/videos"
    cpath = "../db/youtube/channels"

    for channel in os.listdir(vpath):
        d = rss.YoutubeChannel(
            id=channel
        )
        latest = d.latestVideo()
        if latest.id != read_file(vpath + '/' + channel):
            write_file(vpath + '/' + channel, latest.id)
            users = open(cpath + '/' + channel).readlines()
            i = 0
            pings = []
            while i < len(users):
                pings.append(f"<a href='https://matrix.to/#/{users[i]}'>user</a>")
                i += 1
            message = (
f"""
<h1>New upload from {d.author()}</h1>
Subscribers: {', '.join(pings)} <br>
<br> <br>
{latest.title}
<br>
{latest.url()}
"""
            )
            sys.argv[0] = "matrix-commander"
            sys.argv.extend(["-m", f"{message}"])
            sys.argv.extend(["--html"])

            matrix_commander.main()
            
youtube()
sys.exit()
