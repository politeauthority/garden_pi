#!/usr/bin/python                                                                                                
# Weather Model
# This model controls interactions with the indoor and outdoor weather actions which need to occur
import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header

import time
Mysql = MVC.loadDriver('Mysql')

class ModelWeather( object ):

  def get_current( self ):
    last = Mysql.ex( "SELECT * FROM %s.weather ORDER BY `id` DESC LIMIT 1;" % MVC.db['name']  )
    if last:
      return last[0]

  def get_stats( self, seconds_back = 86400 ):
    from datetime import date, datetime, time, timedelta
    dt = datetime.now() - timedelta( seconds = seconds_back )
    sql = "SELECT * FROM garden.weather WHERE `date` > '%s' ORDER BY `id` DESC;" % dt
    stats = Mysql.ex( sql )
    return stats
  
  def get_min_max( self, seconds_back = 86400 ):
    from datetime import date, datetime, time, timedelta
    dt = datetime.now() - timedelta( seconds = seconds_back )
    indoor_temp_min = Mysql.ex( "SELECT MIN( indoor_temp_f ) FROM %s.weather WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    indoor_temp_avg = Mysql.ex( "SELECT AVG( indoor_temp_f ) FROM %s.weather WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    indoor_temp_avg = round( indoor_temp_avg[0][0], 1 )
    indoor_temp_max = Mysql.ex( "SELECT MAX( indoor_temp_f ) FROM %s.weather WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    indoor_hum_min  = Mysql.ex( "SELECT MIN( indoor_humidity ) FROM %s.weather WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    indoor_hum_avg  = Mysql.ex( "SELECT AVG( indoor_humidity ) FROM %s.weather WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    indoor_hum_avg  = round( indoor_hum_avg[0][0], 1 )
    indoor_hum_max  = Mysql.ex( "SELECT MAX( indoor_humidity ) FROM %s.weather WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )

    outdoor_temp_min = Mysql.ex( "SELECT MIN( outdoor_temp_f ) FROM %s.weather WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    outdoor_temp_avg = Mysql.ex( "SELECT AVG( outdoor_temp_f ) FROM %s.weather WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    outdoor_temp_avg = round( outdoor_temp_avg[0][0], 1 )
    outdoor_temp_max = Mysql.ex( "SELECT MAX( outdoor_temp_f ) FROM %s.weather WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    outdoor_hum_min  = Mysql.ex( "SELECT MIN( outdoor_humidity ) FROM %s.weather WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    outdoor_hum_avg  = Mysql.ex( "SELECT AVG( outdoor_humidity ) FROM %s.weather WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    outdoor_hum_avg  = round( outdoor_hum_avg[0][0], 1 )
    outdoor_hum_max  = Mysql.ex( "SELECT MAX( outdoor_humidity ) FROM %s.weather WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    results = {
      'indoor_temp_min'      : indoor_temp_min[0][0],
      'indoor_temp_avg'      : indoor_temp_avg,
      'indoor_temp_max'      : indoor_temp_max[0][0],
      'indoor_humidity_min'  : indoor_hum_min[0][0],
      'indoor_humidity_avg'  : indoor_hum_avg,
      'indoor_humidity_max'  : indoor_hum_max[0][0],
      'outdoor_temp_min'     : outdoor_temp_min[0][0],
      'outdoor_temp_avg'     : outdoor_temp_avg,
      'outdoor_temp_max'     : outdoor_temp_max[0][0],
      'outdoor_humidity_min' : outdoor_hum_min[0][0],
      'outdoor_humidity_avg' : outdoor_hum_avg,
      'outdoor_humidity_max' : outdoor_hum_max[0][0],
    }
    return results

  def store_info( self, outdoor, indoor ):
    info = {
      'indoor_temp_f'        : indoor['temp_f'],
      'indoor_humidity'      : indoor['humidity'],
      'outdoor_temp_f'       : outdoor['temp_f'],
      'outdoor_temp_f_feels' : outdoor['temp_f_feel'],
      'outdoor_humidity'     : outdoor['humidity'],
      'date'                 : time.strftime("%Y-%m-%d %H:%M:%S")
    }
    Mysql.insert( 'weather', info )

# End File: models/ModelWeather.py
