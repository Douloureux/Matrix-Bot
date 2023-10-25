import update_report
import subprocess
import schildichat
import powershell
import element
import sys
from lib import matrix_commander

subprocess.call(['sudo','apt','update'])

schildi = update_report.schildi_update_reporter() 
elementup = update_report.element_update_reporter()
pwsh = update_report.powershell_update_reporter()

if schildi:
    schildichat.update_schildi()

if elementup:
    element.update_element()

if pwsh:
    powershell.update_powershell()

update_message = (
f"""
# Daily Update Report

+ {update_report.sys_update_reporter()}

+ {update_report.synapse_update_reporter()}

{'+ Element was updated to the latest version.' if elementup else '+ Element is up to date.'}

{'+ SchildiChat was updated to the latest version.' if schildi else '+ SchildiChat is up to date.'}

{'+ PowerShell was updated to the latest version.' if pwsh else '+ PowerShell is up to date.'}
"""
)

sys.argv[0] = "matrix-commander"
sys.argv.extend(["-m", f"{update_message}"])
sys.argv.extend(["--markdown"])

matrix_commander.main()

sys.exit()