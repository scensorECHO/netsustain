#! /usr/bin/python

import sys
import os
import subprocess

# for line in sys.stdin:
# 	sys.stdout.write(line)

ssids = ["OCC-Internet","ATT3X792x9", "grizznet"]

# os.system("date")
subprocess.call("date")
#subprocess.call(["cd","/home/tom/"])
#subprocess.call(["ls","-l","-a","/home/tom"])
# out = subprocess.check_output(["ls","-l","-a","/home/tom"],universal_newlines=True).split('\n')
# #directory = []
# for one in out:
# 	print(one)

# str1 = subprocess.check_output(["ip","addr"],universal_newlines=True).split('\n')
# for i in str1:
#    print(i)

# str2 = subprocess.check_output(["ip","addr"],universal_newlines=True).split('\n')
# for i in str2:
#    if "inet" in i:
#        myi = (i.split(' '))
#        print(myi[4]+" "+myi[5]+" "+myi[-1])

str3 = subprocess.check_output(["iw","dev"])
if "Interface " in str3:
	str3 = x[10:]

def findNetwork():
selection = ""
str4 = subprocess.check_output(["iw","dev",str3,"scan","|","grep","SSID"])
for ssid in str4:
	if ssid in ssids:
		selection=ssid
		connect()

def connect():
connection = subprocess.check_output("iw","dev",str3,"connect",selection)
if "connected" in connection:
	print("Successfully connected")
	return true
else:
	print("Failed to connect")
	return false