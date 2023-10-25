import os
from utils import updates
import urllib.request
import shutil
import tarfile

VERSION = str(updates.latest_tag("SchildiChat", "schildichat-desktop"))

def update_schildi():
    shutil.move("/home/user/schildichat/config.json", "/home/user/config.json")

    url = f"https://github.com/SchildiChat/schildichat-desktop/releases/download/{VERSION}/schildichat-web-{VERSION.replace('v', '')}.tar.gz"
    output_file = "/home/user/schildichat-web.tar.gz"
    with urllib.request.urlopen(url) as response, open(output_file, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    shutil.rmtree("/home/user/schildichat")

    tar = tarfile.open(output_file)
    tar.extractall("/home/user")
    tar.close()

    os.remove(output_file)
    os.rename(f"/home/user/schildichat-web-{VERSION.replace('v', '')}", "/home/user/schildichat")
    shutil.move("/home/user/config.json", "/home/user/schildichat/config.json")