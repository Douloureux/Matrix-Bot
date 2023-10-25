import os
from utils import updates
import urllib.request
import shutil
import tarfile

VERSION = str(updates.latest_tag("vector-im", "element-desktop"))

def update_element():
    shutil.move("/home/user/element/config.json", "/home/user/config.json")

    url = f"https://github.com/vector-im/element-web/releases/download/{VERSION}/element-{VERSION}.tar.gz"
    output_file = "/home/user/element-web.tar.gz"
    with urllib.request.urlopen(url) as response, open(output_file, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    shutil.rmtree("/home/user/element")

    tar = tarfile.open(output_file)
    tar.extractall("/home/user")
    tar.close()

    os.remove(output_file)
    os.rename(f"/home/user/element-{VERSION}", "/home/user/element")
    shutil.move("/home/user/config.json", "/home/user/element/config.json")