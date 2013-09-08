#!/usr/bin/python
# Main Cron
# Here we figure out what we need to run, and we execute it, every 10 minutes
import sys
import os
from datetime import date, datetime, time, timedelta

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header

import subprocess
from time import strptime


# Read the SHT15 temperature/humidity sensor, log it
Mysql    = MVC.loadDriver( 'Mysql' )
I2c      = MVC.loadDriver( 'I2c' )
Settings = MVC.loadHelper( 'Settings' )
Logger   = MVC.loadHelper( 'Logger' )


weatherunder = Settings.get_option( 'use-network-weatherunderground' )
use_alerts   = Settings.get_option( 'use-alert' )

AlertModel   = MVC.loadModel( 'Alert' )
WeatherModel = MVC.loadModel( 'Weather' )
WaterModel   = MVC.loadModel( 'Water' )

Logger.write( 'Starting Regular Cron', '', 'cron' )

# Check all our sensors and run all our tasks
if Settings.get_option('use-network-weatherunderground'):
  print 'Weather Underground'
  WeatherUnderAPI = MVC.loadDriver( 'WeatherUnderAPI' )
  OutsideWeather  = WeatherUnderAPI.run()
  Logger.write( '    Weather Underground', 'Pulled and stored local weather', 'cron' )

if Settings.get_option('use-sensor-shtx'):
  import ast
  print 'Reading sht1x'
  hardware_path = '%shardware.py' % MVC.garden_dir
  proc = subprocess.Popen( "sudo python %s --read=sht1x" % hardware_path, stdout=subprocess.PIPE, shell=True  )
  text = proc.communicate()[0]

  print text
  insideWeather = ast.literal_eval( text )
  Logger.write( '    Temp/Humidty Sensor','Read and stored values', 'cron' )

# @tdo: Figure out a better method for logging with either inside or outside weather missing
if OutsideWeather and insideWeather:
  WeatherModel.store_info( OutsideWeather, insideWeather )

# I2c bus sensor readings
# @todo: do this through hardware.py --read=I2c-4
sensor_readings = I2c.getStatus( 4 )
if sensor_readings:
  WaterModel.store_info( sensor_readings[0], sensor_readings[1] )


current = WeatherModel.get_current()

# LIGHTING CONFIGURATION
if Settings.get_option( 'use-lighttiming' ):
  start  = Settings.get_option( 'lighttiming-start' ).split(':')
  stop   = Settings.get_option( 'lighttiming-stop' ).split(':')

  checkForJobTo   = datetime.today()
  checkForJobFrom = checkForJobTo - timedelta( seconds = 600 )

  start_time = checkForJobTo.strftime('%Y-%m-%d ') + '%s:%s' % ( start[0], start[1] )
  start_time = datetime( *strptime(start_time, "%Y-%m-%d %H:%M")[0:6] )

  stop_time  = checkForJobFrom.strftime('%Y-%m-%d ') + '%s:%s' % ( stop[0], stop[1] )
  stop_time  = datetime( *strptime(stop_time, "%Y-%m-%d %H:%M")[0:6] )

  #check if its time to turn on
  if checkForJobFrom < start_time < checkForJobTo:
    subprocess.call( "sudo python %shardware.py --lighting=on" % MVC.garden_dir,    shell=True )

  #check if its time to turn off
  if checkForJobFrom < stop_time < checkForJobTo:
    subprocess.call( "sudo python %shardware.py --lighting=off" % MVC.garden_dir,    shell=True )



# Take what we have figured out and figure out if we need to notify anyone
if use_alerts:
  message = False
  if AlertModel.temp_high and float( current[2] ) >= float( AlertModel.temp_high ):
    message = [ 'High Temp Alert!', 'The garden temperature indoor is currently %s F.' % current[2] ]

  if AlertModel.temp_low and float( current[2] ) <= float( AlertModel.temp_low ):
    message = [ 'Low Temp Alert!', 'The garden temperature indoor is currently %s F.' % current[2] ]

  if message:
    Logger.write('    [ALERT] %s' % message[0], message[1], 'cron' )    
    AlertModel.messaging( message )

# End File: cron/main.py
