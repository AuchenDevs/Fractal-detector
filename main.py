import os
from datetime import datetime
import subprocess
import win32gui, win32process

#That was made by craciu25_YT

def getStrings():
    instance = win32gui.FindWindow("LWJGL", None)
    if not instance:
        print("Minecraft instance not found")
        exit()
    print("Instance was found. Taking strings")
    pid = win32process.GetWindowThreadProcessId(instance)[1]
    # 2.75% more fast deleting past file
    if os.path.isdir(f"{os.environ.get('TEMP')}\\FractalChecker\\"):
        if os.path.exists(f"{os.environ.get('TEMP')}\\FractalChecker\\strings.txt"):
            os.remove(f"{os.environ.get('TEMP')}\\FractalChecker\\strings.txt")
    else: 
        os.mkdir(f"{os.environ.get('TEMP')}\\FractalChecker")

    start = datetime.now()
    os.popen(f"{os.path.dirname(os.path.abspath(__file__))}\\string.exe -p {pid} > %temp%\\FractalChecker\\strings.txt").read()
    print("Strings took ", datetime.now() - start, "to be exported!")



def fractal():
    getStrings()
    with open(f"{os.environ.get('TEMP')}\\FractalChecker\\strings.txt", 'r') as file:
        for line in file:
            if "(Ljava/lang/String;)Lxyz/flapjack/fractal/modules/Module;" in line:
                return True
    return False

print("Checking for instance")
if fractal():
    print("Fractal was found injected!")
else:
    print("User is not using fractal")