#! /usr/bin/python
import subprocess

ssids = ["OCC-Internet","ATT3X792x9", "grizznet"]

def devSelect():
	str3 = subprocess.check_output(["iw","dev"],universal_newlines=True).split('\n')
	for line in str3:
		if "Interface " in str3:
			str3 = str3.split( )[1]
			return str3
		else:
			return "failed"

def findNetwork(dev):
	selection = ""
	str4 = subprocess.check_output(["iw","dev",dev,"scan","|","grep","SSID"],universal_newlines=True).split('\n')
	for ssid in str4:
		if ssid in ssids:
			selection=ssid
			return connect(selection)

def connect(dev, sel):
	connection = subprocess.check_output(["iw","dev",dev,"connect","-w",sel],universal_newlines=True).split('\n')
	if "connected" in connection:
		print("Successfully connected")
		return true
	else:
		print("Failed to connect")
		return false

def runDHCP(dev):
	result = subprocess.check_output(["dhcpcd",dev],universal_newlines=True).split('\n')
	if "leased" in result:
		return true
	else:
		return false

device = devSelect()
if "w" in device:
	if(findNetwork(device)):
		if(runDHCP(device)):
			print("Success")
		else:
			print("DHCP failure")
	else:
		print("Network connection error")
else:
	print("No wireless devices found")