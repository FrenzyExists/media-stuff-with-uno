#!/usr/bin/python

import os
import sys
import subprocess

def main():
    data = sys.argv
    
    if data[1]:
        if data[1] in 'vol':
            if data[2] and data[2] in ['up', 'down', 'toggle']:
                try:
                    a = {
                        'up': 'pamixer -i 10',
                        'down': 'pamixer -d 10',
                        'toggle': 'pamixer -t'
                    }
                    subprocess.check_output('pamixer')
                    os.system(a[data[2]])
                except subprocess.CalledProcessError as err:
                    os.system('mpd')
                
            else:
                print("Wrong input, for volume it must be 'up', 'down' or 'toggle'")
                exit()
        elif data[1] in 'brightness':
            if data[2] and data[2] in ['inc', 'dec']:
                try:
                    subprocess.check_output(['xbacklight', '-' + data[2], '10'])
                except subprocess.CalledProcessError as err:
                    print("xbacklight is not installed, either install it or change this script to match the program you use to control your brightness")
                    exit()
            else:
                print("Wrong input, for volume it must be 'inc' or 'dec'")
                exit()
        elif data[1] in 'media':
            if data[2] and data[2] in ['prev', 'next', 'toggle']:
                try:
                    subprocess.check_output('mpc')
                except subprocess.CalledProcessError as err:
                    os.system('mpd')
                os.system('mpc ' + data[2] )
            else:
                print("Wrong input, for volume it must be 'prev', 'next' or 'toggle'")
                exit()
    else:
        print("Wrong input or no input added")
        exit()

if __name__ == "__main__":
    main()