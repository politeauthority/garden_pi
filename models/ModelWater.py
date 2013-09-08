#!/usr/bin/python                                                                                                
# Water Model
# This model controls interactions with the water database interactions
import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header

import time
Mysql = MVC.loadDriver('Mysql')

class ModelWater( object ):

  def get_stats( self, seconds_back = 86400 ):
    from datetime import date, datetime, time, timedelta
    dt = datetime.now() - timedelta( seconds = seconds_back )
    sql = "SELECT * FROM %s.water WHERE `date` > '%s' ORDER BY `id` DESC;" % ( MVC.db['name'], dt )
    # sql = "SELECT * FROM %s.water WHERE `read_time` > '%s' ORDER BY `id` DESC;" % ( 'garden', dt )    
    stats = Mysql.ex( sql )
    return stats

  def store_info( self, temp_1, flow_1 ):
    info = {
      'water_temp_1'        : temp_1,
      'flow_1'              : flow_1,
    }
    Mysql.insert( 'water', info )

# End File: models/ModelWater.py