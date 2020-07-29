import sys
import time
import os

if 'serial' not in sys.modules:
    os.system("python -m pip install pyserial")
if 'playsound' not in sys.modules:
    os.system("python -m pip install playsound")

from serial import Serial
from  playsound import playsound
import json

open_ports = os.popen("ls /dev/cu.*").read().split("\n")
kano_port = ""

for port in open_ports:
    if "cu.usbmodem" in port:
        kano_port = port
        break

if kano_port == "":
    print("Please plug in KANO Motion Sensor to continue")
else:
    s = Serial(kano_port)
    previous_proximity = 0
    status = 0

    def toggleFunction():
        global status

        if status == 0:
            playsound("dog_bark.mp3")
            print("playing sound")
            status = 1
        else:
            playsound("cat_meow.mp3")
            print("playing sound")
            status = 0

    while True:
        try:
            data = json.loads(s.readline())
            proximity = (data["detail"]["proximity"])

            if previous_proximity > 0:
                proximity = 0

            if proximity > 0:
                print("Motion Detected")
                toggleFunction()
                time.sleep(0.2)
            else:
                print("No Motion")

            previous_proximity = proximity

            s.flushInput()
        except Exception:
            continue