#!/usr/bin/python                                                                                                  
# Serial Driver 
# This is the serial comm class
# @requirements( )
import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header

import time               
import serial

Mysql = MVC.loadDriver('Mysql')

class DriverSerial( object ):
  def __init__( self ):
    self.conn()   

  def conn( self ):
    self.ser_con    = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    self.ser_con.open()

  def outlet( self, outlet, enable = False ):
    self.conn()
    if outlet == 1:
      com = 1
    elif outlet == 2:
      com = 3

    if enable == True:
      com = com - 1

    self.ser_con.write( str( com ) )
    return True

# End File: driver/DriverSerial.py
