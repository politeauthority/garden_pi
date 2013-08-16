#!/usr/bin/python
# Hardware.py
# Here we will channel all hardware interactions, 
#   then in turn this script should be run as subprocess in scripts which need it

import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End Header

import getopt



def main(argv):
	try:                                
		opts, args = getopt.getopt(argv, "hg:d", ["help", "d", "lighting=", "read="])
	except getopt.GetoptError:
		usage()
		sys.exit()
	for opt, arg in opts:
		global verbose		
		
		if opt == '-v':
			verbose = 1
		else:
			verbose = 0

			if verbose:
				print 'Hardware.py'

		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-l", "--lighting"):
			print 'Lighting'
			lighting( arg )
		elif opt in ("-r", "--read"):
			if verbose:
				print 'Sensor Reading'
			if arg == 'sht1x':
				print sensor_sht1x()
			else:
				print 'Unknown sensor'
				sys.exit()
		else:
			usage()

def usage():
	print 'Welcome to hardware.py! heres some basic usage'
	print '--lighting: "on" or "off"'
	print '--read: '
	print '   sht1x - temperature/humidity'
	print '--help:     This screen'

def lighting( status ):
	global verbose
	Devices = MVC.loadModel('Devices')
	Devices.lighting( status )
	if verbose:
		print 'Lights have been turned %s' % status
	sys.exit()

def sensor_sht1x():
	global verbose
	if verbose:
		print 'SHTX Sensor'
	GPIO = MVC.loadDriver( 'GPIO' )
	reading = GPIO.read_sht1x()
	return reading

if __name__ == "__main__":
  main( sys.argv[1:] )
  sys.exit()

#End File: hardware.py 