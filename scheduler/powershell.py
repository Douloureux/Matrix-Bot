import subprocess
import os
from utils import updates
import urllib.request
import shutil
import tarfile

VERSION = str(updates.latest_tag("PowerShell", "PowerShell"))
ARCH = subprocess.check_output("arch", shell=True).decode('ascii').strip()

if ARCH == "aarch64":
    ARCH = "arm64"
if ARCH == "x86_64":
    ARCH = "x64"

def update_powershell():
    if os.path.exists("/tmp/powershell"):
        shutil.rmtree("/tmp/powershell")
    os.mkdir("/tmp/powershell")
    url = f"https://github.com/PowerShell/PowerShell/releases/download/{VERSION}/powershell-{VERSION.replace('v','')}-linux-{ARCH}.tar.gz"
    output_file = "/tmp/powershell.tar.gz"
    with urllib.request.urlopen(url) as response, open(output_file, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    
    tar = tarfile.open(output_file)
    tar.extractall("/tmp/powershell")
    tar.close()

    subprocess.call(
        [
            'sudo',
            'rm',
            '-r',
            '/opt/microsoft/powershell/7/*'
        ]
    )

    subprocess.call(
        [
            'sudo',
            'mv',
            '/tmp/powershell/*',
            '/opt/microsoft/powershell/7/'
        ]
    )