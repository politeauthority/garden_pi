#!/usr/bin/python
# Main Cron
# Here we figure out what we need to run, and we execute it, every 10 minutes
import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header

import time

# Read the SHT15 temperature/humidity sensor, log it
Mysql    = MVC.loadDriver('Mysql')
Settings = MVC.loadHelper('Settings')

shtx         = Settings.get_option('use-sensor-shtx')
weatherunder = Settings.get_option('use-network-weatherunderground')
alerts       = Settings.get_option('use-alert')

if shtx:
  print 'the sensor is ready for use'
  GPIO     = MVC.loadDriver('GPIO')
  GPIO.read_sensor()

if weatherunder:
  print 'weather underground is ready for use'
  WeatherUnderAPI = MVC.loadDriver( 'WeatherUnderAPI' )
  WeatherUnderAPI.run()
  
if alerts:
  Prowl = MVC.loadDriver('Prowl')
  alert_temp_high = Settings.get_option('alert-opt-temp-high')
  if Settings.get_option('alert-opt-temp-high') is not None:
    indoor_weather = Mysql.ex("SELECT * FROM %s.weather_indoor ORDER BY id DESC LIMIT 1" % MVC.db['name'] )
    if indoor_weather[0][1] > int( alert_temp_high ):
      apikey  = "aca77c19f5c5bdb2b9d099b3fb569df736192f78"
      message = 'The current indoor temperature is %sF with %s humidity, recorded at %s' % ( str(indoor_weather[0][1]), str(indoor_weather[0][2]), indoor_weather[0][3] )

      Prowl.send( apikey, 'High Temperature Alert', message, 1)


#sensor = GPIO.read_sht1x()

#Mysql.ex("INSERT INTO `garden`.`weather_indoor` (`temp_f`, `humidity`, `date`) VALUES ( '%s', '%s', '%s' )" % ( sensor[1], sensor[2], time.strftime("%Y-%m-%d %H:%M:%S") ) )

#print( "Temperature: {} Humidity: {} Dew Point: {}".format( sensor[1], sensor[2], sensor[3] ) )

# Grab the local weather from the weather underground


#End File: cron/main.py
