#! /usr/bin/python

import sys
import os

for line in sys.stdin:
	sys.stdout.write(line)

sys.stdout.write(os.system("date"))