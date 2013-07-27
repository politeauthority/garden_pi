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
Logger   = MVC.loadHelper('Logger')

shtx         = Settings.get_option('use-sensor-shtx')
weatherunder = Settings.get_option('use-network-weatherunderground')
alerts       = Settings.get_option('use-alert')

Logger.write('Starting Regular Cron', '', 'cron' )
if shtx:
  GPIO     = MVC.loadDriver('GPIO')
  GPIO.read_sensor()
  Logger.write( 'Temp/Humidty Sensor','Read and stored values', 'cron' )

if weatherunder:
  WeatherUnderAPI = MVC.loadDriver( 'WeatherUnderAPI' )
  WeatherUnderAPI.run()
  Logger.write( 'Weather Underground', 'Pulled and stored local weather', 'cron' )
  
if alerts:
  Prowl = MVC.loadDriver('Prowl')
  alert_temp_high = Settings.get_option('alert-opt-temp-high')
  if Settings.get_option('alert-opt-temp-high') is not None:
    indoor_weather = Mysql.ex("SELECT * FROM %s.weather_indoor ORDER BY id DESC LIMIT 1" % MVC.db['name'] )
    if int(indoor_weather[0][1]) > int( alert_temp_high ):
      apikey  = "aca77c19f5c5bdb2b9d099b3fb569df736192f78"
      message = 'The current indoor temperature is %sF with %s humidity, recorded at %s' % ( str(indoor_weather[0][1]), str(indoor_weather[0][2]), indoor_weather[0][3] )
      Prowl.send( apikey, 'High Temperature Alert', message, 1)

# End File: cron/main.py
