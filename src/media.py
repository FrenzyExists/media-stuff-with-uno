#!/usr/bin/python

import os
import sys
import subprocess

def main():
    data = sys.argv
    
    if data[1] and data[1] in ['prev', 'next', 'toggle']:
        try:
            subprocess.check_output('mpc')
        except subprocess.CalledProcessError as err:
            os.system('mpd')
        os.system('mpc ' + data[1] )
    else:
        print("Wrong input or no input added")
        exit()

if __name__ == "__main__":
    main()