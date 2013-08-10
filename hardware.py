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



print 'Hardware.py'


def main(argv):                         
	grammar = "kant.xml"                
	try:                                
		opts, args = getopt.getopt(argv, "hg:d", ["help", "lighting="])
	except getopt.GetoptError:
		usage()
		sys.exit()
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt == '-d':
			global _debug               
			_debug = 1                  
		elif opt in ("-l", "--lighting"):
			print 'Lighting'
			lighting( arg )
		else:
			print 'here'

def usage():
	print '--lighting: "on" or "off"'
	print '--help:     This screen'

def lighting( status ):
	Devices = MVC.loadModel('Devices')
	Devices.lighting( status )	
	print 'Lights have been turned %s' % status
	sys.exit()




if __name__ == "__main__":
  main( sys.argv[1:] )
  sys.exit()

#End File: hardware.py 