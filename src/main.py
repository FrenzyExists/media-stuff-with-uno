#!/usr/bin/python
import os
import serial
import time

PATH=os.path.dirname(os.path.abspath(__file__)) # Change this to your path if it doesn't work

commando = {
    'V-DOWN': PATH + '/media.py vol down',
    'V-UP':   PATH + '/media.py vol up',
    'V-MUTE': PATH + '/media.py vol toggle',
    'B-UP':   PATH + '/media.py brightness inc',
    'B-DOWN': PATH + '/media.py brightness dec',
    'PLAY':   PATH + '/media.py media toggle',
    'NEXT':   PATH + '/media.py media next',
    'PREV':   PATH + '/media.py media prev',
}


def main():
    print("FIRING UP")
    try:
        ser = serial.Serial(
            port='/dev/ttyUSB0', 
            baudrate=9660,
            timeout=1
        )
        ser.isOpen() # try to open port, if possible print message and proceed with 'while True:'
        print("port is opened!")
    except IOError:
        ser.close()
        ser.open()
        print ("port was already open, was closed and opened again!")

    time.sleep(1)
    while True:
        var = ser.readline().decode('utf-8').strip()
        if var != "":
            print(var, end="")
            os.system(commando[var])
if __name__ == "__main__":
    main()