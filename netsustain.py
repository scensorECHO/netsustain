#! /usr/bin/python

import sys
import os
import subprocess

for line in sys.stdin:
	sys.stdout.write(line)

os.system("date")
subprocess.call("date")
subprocess.call("ls","-l","-a")
