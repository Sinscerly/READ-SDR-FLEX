#!/usr/bin/python

import os

os.system("rtl_fm -f 169.65M -M fm -s 22050 -p 43 -g 49 | multimon-ng -a FLEX -t raw /dev/stdin")



