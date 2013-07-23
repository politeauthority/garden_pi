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
import RPi.GPIO as GPIO                      

Mysql = MVC.loadDriver('Mysql')

class DriverGPIO( object ):
  def __init__( self ):
    self.water_pump = 18

  def pump_toggle( self ):
    pump_status = self.pump_status()        
    if pump_status:
      query = "UPDATE garden.device_runtime SET date_off = '%s' WHERE id = '%s';" % ( time.strftime("%Y-%m-%d %H:%M:%S"), pump_status[0][0] )
      set_value = False
    else:
      query = "INSERT INTO garden.device_runtime ( device_id, date_on, date_off) VALUES( %s, '%s', %s);" % ( 1, time.strftime("%Y-%m-%d %H:%M:%S"), "NULL" )
      set_value = True
    Mysql.ex( query )
    GPIO.setmode( GPIO.BCM )
    GPIO.setup( self.water_pump, GPIO.OUT )
    GPIO.output( self.water_pump, set_value )
    return query

  def pump_status( self, give_back = False ):
      previously_on = Mysql.ex( "SELECT * FROM garden.device_runtime WHERE device_id = 1 ORDER BY id DESC LIMIT 1;" )
      if previously_on and previously_on[0][3]:
        if give_back:
          return False
        else:
          return previously_on 
        print 'the pump is off'
      else:
        print 'the pump is off'

      print previously_on
      if previously_on:
        return previously_on
      else:
        return False
    
  def read_sensor( self ):
    from sht1x.Sht1x import Sht1x as SHT1x
    dataPin = 24
    clkPin  = 22
    sht1x   = SHT1x(dataPin, clkPin, SHT1x.GPIO_BCM)

    temp_c      = sht1x.read_temperature_C()
    temp_f      = round( ( temp_c * ( 9.0 / 5.0 ) ) + 32, 1 )
    humidity    = round( sht1x.read_humidity(), 0 )
    dewPoint    = sht1x.calculate_dew_point( temp_c, humidity )

    values      = {
      'temp_f'   : temp_f,
      'humidity' : humidity,
      'date'     : time.strftime("%Y-%m-%d %H:%M:%S")
    }
    Mysql.insert( 'weather_indoor', values )
    return [ temp_c, temp_f, humidity, dewPoint ]
