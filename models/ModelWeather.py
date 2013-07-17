#!/usr/bin/python                                                                                                
# Weather Model
# This model controls interactions with the indoor and outdoor weather actions which need to occur
import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header


Mysql = MVC.loadDriver('Mysql')

class ModelWeather( object ):

    def get_current_indoor( self ):
        last = Mysql.ex( "SELECT * FROM garden.weather_indoor ORDER BY `id` DESC LIMIT 1;" )
        return last[0]

    def get_stats_indoor( self, seconds_back = 86400 ):
        stats = Mysql.ex( "SELECT * FROM garden.weather_indoor" )
        return stats

# End File: models/ModelWeather.py
