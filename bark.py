import serial, json
import time
import os

s = serial.Serial('/dev/cu.usbmodem14101')
status = 0

def toggleFunction():
    global status

    if status == 0:
        os.system("open -a Terminal")
        status = 1
    else:
        os.system("open -a Terminal")
        status = 1

while True:
    try:
        data = json.loads(s.readline())
        proximity = (data["detail"]["proximity"])

        print(proximity)

        if proximity > 0:
            toggleFunction()
            print("\n\n\n\n" + lights_status + "\n\n\n\n")
            time.sleep(3)

        s.flushInput()
    except Exception:
        continue
