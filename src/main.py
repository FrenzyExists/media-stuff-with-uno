#!/usr/bin/python
import os
import serial
import time

commando = {
    'V-DOWN': '/home/pikachu/.scripts/notification/volume_pam.sh down',
    'V-UP': '/home/pikachu/.scripts/notification/volume_pam.sh up',
    'V-MUTE': '/home/pikachu/.scripts/notification/volume_pam.sh toggle',
    'B-UP': '/home/pikachu/.scripts/notification/brightness.sh up',
    'B-DOWN': '/home/pikachu/.scripts/notification/brightness.sh down',
    'PLAY': '/home/pikachu/Documents/PlatformIO/Projects/Uno-scripting/src/media.py toggle',
    'NEXT': '/home/pikachu/Documents/PlatformIO/Projects/Uno-scripting/src/media.py next',
    'PREV': '/home/pikachu/Documents/PlatformIO/Projects/Uno-scripting/src/media.py prev',
}


def main():
    print("FIRING UP")
    ser = serial.Serial('/dev/ttyUSB0', 9660, timeout=1)
    time.sleep(1)
    while True:
        var = ser.readline().decode('utf-8').strip()
        if var != "":
            print(var, end="")
            os.system(commando[var])
if __name__ == "__main__":
    main()