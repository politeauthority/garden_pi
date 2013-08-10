#!/usr/bin/python                                                                                                
# Devices Model
# This model will manage the garden appliances, such as lights, pumps, feeders
import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header

Mysql = MVC.loadDriver('Mysql')
Settings = MVC.loadHelper('Settings')

class ModelDevices( object ):

  def __init__( self ):
    self.temp_high = Settings.get_option('alert-opt-temp-high')
    self.temp_low  = Settings.get_option('alert-opt-temp-low')

  def lighting( self, status ):
    Serial = MVC.loadDriver('Serial')
    if status == 'on':
      status = True
    elif status == 'off':
      status = False
    else:
      print 'ERROR must have on/off status'
      sys.exit()

    for light in self.get_lights():
      Serial.outlet( light[3], status )
      self.log_use( light[0], 0, status )

  def get_lights( self ):
    sql  = "SELECT * FROM %s.devices WHERE `type`= 'light' " % MVC.db['name']
    lights = Mysql.ex( sql )
    return lights

  def log_use( self, device_id, user_id, state ):
    from datetime import date, datetime, time, timedelta
    if state == True:
      state = 1
    else:
      state = 0
    info = {
      'device_id' : device_id,
      'user_id'   : user_id,
      'state'     : state,
      'date'      : datetime.now()
    }
    Mysql.update( 'devices', {'status_bit': '1'}, ['id', device_id] )
    Mysql.insert( 'devices_log', info )

# End File: models/ModelDevices.py