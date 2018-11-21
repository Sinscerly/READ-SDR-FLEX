#!/usr/bin/python

#TEST FILE, SO NOT FINAL SCRIPT!!!

#SETTINGS:
file_with_capcodes      = 'test_capcodes.txt'
file_for_output_lines   = 'output.txt'
file_for_error_logging  = 'error.txt'

#DEFINED
clean = True

import subprocess
import time
import sys
import os
#import re

def curtime():
    return time.strftime("%H:%M:%S %Y-%m-%d")

with open(file_for_error_logging, 'a') as file:
    file.write(('#' * 20) + '\n' + curtime() + '\n')

result = subprocess.Popen("rtl_fm -f 169.65M -M fm -s 22050 -p 43 -g 49 | multimon-ng -a FLEX -t raw -",
        stdout=subprocess.PIPE,
        stderr=open(file_for_error_logging,'a'),
        shell=True)

f = open(file_for_output_lines, 'a')
old_out = ''
try: 
    while True:
        dataline = result.stdout.readline()
        result.poll()
        if dataline != b"":
            out = dataline.decode('utf-8')
            if out.startswith('FLEX')   and \
                    'ALN' in out        and \
                    out != old_out      and \
                    'test' not in out:
                        #Strip the line into pieces
                        flex        = out[0:5]
                        timestamp   = out[6:25]
                        code1       = out[26:36]
                        code2       = out[37:43]
                        capcode     = out[45:54]
                        aln         = out[56:59]
                        melding     = out[58:]
                        
                        caps = open(file_with_capcodes, 'r')
                        for line in caps.readlines():
                            #print ("capcode:" + capcode + "---" + line),
                            if line.startswith(capcode):
                                print (out)
                                f.write(out)
                                #execute trigger/action....

                        caps.close()

                        #For testing with stripping line:
                        if clean is not True:
                            print (timestamp),
                            #print (code1),
                            #print (code2),
                            print (code3),
                            #print (aln),
                            #print (code4)
                        
                        #For preventing double lines
                        old_out = out

except KeyboardInterrupt:
    os.kill(result.pid, 9)
