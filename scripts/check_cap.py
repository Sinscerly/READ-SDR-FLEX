#!/usr/bin/python

i=0
f=open("capcodes.txt", "r")
for line in f.readlines():
    if line.startswith("001220499"):
        print ("yes"),
    else:
        print ("no"),
    print (line)



