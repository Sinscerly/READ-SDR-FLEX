#!/usr/bin/python

clean = True

import subprocess
import time
import sys
import os
import re

def curtime():
    return time.strftime("%H:%M:%S %Y-%m-%d")

with open('error.txt', 'a') as file:
    file.write(('#' * 20) + '\n' + curtime() + '\n')

result = subprocess.Popen("rtl_fm -f 169.65M -M fm -s 22050 -p 43 -g 49 | multimon-ng -a FLEX -t raw -",
        stdout=subprocess.PIPE,
        stderr=open('error.txt','a'),
        shell=True)

try: 
    while True:
        line = result.stdout.readline()
        result.poll()
        
        if line != b"":
            print (line.decode("utf-8")),
            
            #Implement here your own code, what you want to do, create an action... etc...

except KeyboardInterrupt:
    os.kill(result.pid, 9)
