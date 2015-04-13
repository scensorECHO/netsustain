#! /usr/bin/python

import sys
import os

for line in sys.stdin:
	sys.stdout.write(line)

os.system("date")