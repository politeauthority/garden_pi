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

  def get_current_indoor( self ):
    last = Mysql.ex( "SELECT * FROM %s.weather_indoor ORDER BY `id` DESC LIMIT 1;" % MVC.db['name']  )
    if last:
      return last[0]

  def get_current_outdoor( self ):
    last = Mysql.ex( "SELECT * FROM %s.weather_outdoor ORDER BY `id` DESC LIMIT 1;" % MVC.db['name']  )
    return last[0]

  def get_stats_indoor( self, seconds_back = 86400 ):
    from datetime import date, datetime, time, timedelta
    dt = datetime.now() - timedelta( seconds = seconds_back )
    sql = "SELECT * FROM garden.weather_indoor WHERE `date` > '%s' ORDER BY `id` DESC;" % dt
    stats = Mysql.ex( sql )
    return stats
  
  def get_stats_outdoor( self, seconds_back = 86400 ):
    from datetime import date, datetime, time, timedelta
    dt = datetime.now() - timedelta( seconds = seconds_back )
    sql = "SELECT * FROM garden.weather_indoor WHERE `date` > '%s' ORDER BY `id` DESC;" % dt
    stats = Mysql.ex( sql )
    return stats

  def get_stats_chart( self, seconds_back = 86400 ):
    from datetime import date, datetime, time, timedelta
    dt = datetime.now() - timedelta( seconds = seconds_back )
    
    # sql = "SELECT * FROM garden.weather_indoor WHERE `date` > '%s' ORDER BY `id` DESC;" % dt
    # indoor = Mysql.ex( sql )

    sql = "SELECT * FROM garden.weather_outdoor WHERE `date` > '%s' ORDER BY `id` DESC;" % dt
    outdoor = Mysql.ex( sql )

    return outdoor

  def get_min_max( self, seconds_back = 86400 ):
    from datetime import date, datetime, time, timedelta
    dt = datetime.now() - timedelta( seconds = seconds_back )
    temp_min = Mysql.ex( "SELECT MIN( temp_f ) FROM %s.weather_indoor WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    temp_avg = Mysql.ex( "SELECT AVG( temp_f ) FROM %s.weather_indoor WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    temp_avg = round( temp_avg[0][0], 1 )
    temp_max = Mysql.ex( "SELECT MAX( temp_f ) FROM %s.weather_indoor WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    hum_min  = Mysql.ex( "SELECT MIN( humidity ) FROM %s.weather_indoor WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    hum_avg  = Mysql.ex( "SELECT AVG( humidity ) FROM %s.weather_indoor WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    hum_avg  = round( hum_avg[0][0], 1 )
    hum_max  = Mysql.ex( "SELECT MAX( humidity ) FROM %s.weather_indoor WHERE `date` > '%s';" % ( MVC.db['name'], dt ) )
    results = {
      'temp_min'      : temp_min[0][0],
      'temp_avg'      : temp_avg,
      'temp_max'      : temp_max[0][0],
      'humidity_min'  : hum_min[0][0],
      'humidity_avg'  : hum_avg,
      'humidity_max'  : hum_max[0][0], 
    }
    return results



# End File: models/ModelWeather.py