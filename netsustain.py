#! /usr/bin/python
import subprocess
import sh

ssids = []
log = []

subprocess.call(['rm','/etc/netsustain/log'])
subprocess.call(['touch','/etc/netsustain/log'])

with open('/etc/netsustain/ssid') as f:
	content = f.readlines()
	for line in content:
		ssids.append(line.rstrip('\n').split(','))

#print(ssids)

def getWiFiDev():
	log.append('Searching devices')
	devices = subprocess.check_output(["iw","dev"],universal_newlines=True).split('\n\t')
	for line in devices:
		if "Interface " in line:
			interface = line.split()[1]
			log.append("Found interface "+interface)
			return interface
	log.append('No interface found')
	return "failed"

def setupDevice(dev):
	log.append('Setting up device'+dev)
	subprocess.call(["ip","link","set",dev,"up"])
	return

def findNetwork(dev):
	selection = ""
	#str4 = subprocess.check_output(["iw","dev",dev,"scan","|","grep","SSID:"],universal_newlines=True).split('\n')
	nearby = subprocess.check_output(["iw","dev",dev,"scan"],universal_newlines=True).split('\n\t')
	for line in nearby:
		#ssid = ssids[0]
		for ssid in ssids:
			if ssid[0] in line:
				selection=ssid[0]
				log.append('SSID found: '+selection)
	if(selection != ""):
		log.append('Connecting to network: '+selection)
		return connect(dev, selection)
	else:
		log.append('No trusted networks found')
		return 0

def connect(dev, sel):
	connection = subprocess.check_output(["iw","dev",dev,"connect","-w",sel],universal_newlines=True).split('\n')
	for line in connection:
		if "connected" in line:
			print("Successfully connected")
			return 1
		else:
			print("checking next")
	print("Failed to connect")
	return 0

def runDHCP(dev, killed=0):
	result = subprocess.check_output(["dhcpcd"],universal_newlines=True).split('\n')
	if "leased" in result:
		log.append('DHCP IP address leased')
		return 1
	elif "running" in result:
		if !killed:
			log.append('Killing previous dhcpcd process')
			subprocess.call(['pkill','-15','dhcpcd'])
			runDHCP(dev, 1)
		else:
			log.append('Attempt to kill process failed')
	else:
		log.append('No lease acquired')
		return 0

def writeLog():
	with open("/etc/netsustain/log", "a") as logfile:
		for line in log:
			logfile.write(line)


#wifi device setup and connection
device = getWiFiDev()
try:
	if "w" in device:
		setupDevice(device)
		if(findNetwork(device)):
			if(runDHCP(device)):
				print("Success")
			else:
				print("DHCP failure")
		else:
			print("Network connection error")
	else:
		print("No wireless devices found")
except:
	writeLog()