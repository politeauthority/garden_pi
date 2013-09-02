#!/usr/bin/python                                                                                                  
# GPIO Driver 
# This is the GPIO class wrapper for unified communication with the GPIO chipset
# @requirements( )
import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header

                    
import time
import smbus

class DriverI2c( object ):

  def __init__( self ):
    self.bus = smbus.SMBus(0)

  def getStatus( self, device ):
    Formula = MVC.loadHelper('Formula')
    status = ""
    try:
      for i in range (0, 30):
        status += chr( self.bus.read_byte(device) )
        time.sleep(0.05);
      time.sleep(0.1)
    except:
      Alert = MVC.loadModel('Alert')
      Alert.messaging( ['I2C Bus Issue', 'There is a problem reading the I2c bus, we cannot collect data at this time.'] )
      return False

    sensors = [ 'water-temp', 'flow-rate' ]
    status = status.split('x')
    # water temp
    status[0] = Formula.celcius_to_fahrenheit( float( str( status[0][0:-1] ).replace(',','') + '.' + str( status[0][-1] ).replace(',','') )   )# Adjusted because the sensor doesnt put a decimal place in
    
    status[1] = status[1].split('.')
    status[1] = str( status[1][0][0:-1] + '.' + status[1][0][-1] )
    return status

# End File: drivers/DriverI2c.py