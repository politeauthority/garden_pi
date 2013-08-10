#!/usr/bin/python
# Main Cron
# Here we figure out what we need to run, and we execute it, every 10 minutes
import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header

from datetime import date, datetime, time, timedelta

# Read the SHT15 temperature/humidity sensor, log it
Mysql    = MVC.loadDriver('Mysql')
Settings = MVC.loadHelper('Settings')
Logger   = MVC.loadHelper('Logger')


weatherunder = Settings.get_option('use-network-weatherunderground')
alerts       = Settings.get_option('use-alert')

Weather = MVC.loadModel( 'Weather')  

Logger.write('Starting Regular Cron', '', 'cron' )

# Check all our sensors and run all our tasks
if Settings.get_option('use-network-weatherunderground'):
  WeatherUnderAPI = MVC.loadDriver( 'WeatherUnderAPI' )
  OutsideWeather  = WeatherUnderAPI.run()
  Logger.write( '    Weather Underground', 'Pulled and stored local weather', 'cron' )

if Settings.get_option('use-sensor-shtx'):
  GPIO          = MVC.loadDriver('GPIO')
  insideWeather = GPIO.read_sht1x()
  Logger.write( '    Temp/Humidty Sensor','Read and stored values', 'cron' )

if OutsideWeather or insideWeather:
  Weather.store_info( OutsideWeather, insideWeather )

current = Weather.get_current()

# LIGHTING CONFIGURATION
if Settings.get_option( 'use-lighttiming' ):
  from time import strptime
  import subprocess

  start  = Settings.get_option( 'lighttiming-start' ).split(':')
  stop   = Settings.get_option( 'lighttiming-stop' ).split(':')

  checkForJobTo   = datetime.today()
  checkForJobFrom = checkForJobTo - timedelta( seconds = 600 )

  start_time = checkForJobTo.strftime('%Y-%m-%d ') + '%s:%s' % ( start[0], start[1] )
  start_time = datetime( *strptime(start_time, "%Y-%m-%d %H:%M")[0:6] )

  stop_time  = checkForJobFrom.strftime('%Y-%m-%d ') + '%s:%s' % ( stop[0], stop[1] )
  stop_time = datetime( *strptime(stop_time, "%Y-%m-%d %H:%M")[0:6] )

  #datetime(*strptime(s, "%Y-%m-%dT%H:%M:%S")[0:6])
  print start_time
  print stop_time

  if checkForJobFrom < start_time < checkForJobTo:
    subprocess.call( "python %shardware.py --lighting=on" % MVC.garden_dir,    shell=True )
    print 'start: its time to work!'
  else:
    print 'stop: not time for shit'

  if checkForJobFrom < stop_time < checkForJobTo:
    subprocess.call( "python %shardware.py --lighting=off" % MVC.garden_dir,    shell=True )
    print 'start: its time to work!'

  else:
    print 'stop: not time for shit'

  print checkForJobFrom
  print checkForJobTo

# Take what we have figured out and figure out if we need to notify anyone
if alerts:
  Alert = MVC.loadModel('Alert')

  message = False

  if Alert.temp_high and float( current[1] ) >= float( Alert.temp_high ):
    message = [ 'High Temp Alert!', 'The garden temperature indoor is currently %s F.' % current[1] ]

  if Alert.temp_low and float( current[1] ) <= float( Alert.temp_low ):
    message = [ 'Low Temp Alert!', 'The garden temperature indoor is currently %s F.' % current[1] ]
    

  if message:
    Logger.write('    [ALERT] %s' % message[0], message[1], 'cron' )    
    Alert.messaging( message )

Logger.write( ' ', '', 'cron' );

# End File: cron/main.py