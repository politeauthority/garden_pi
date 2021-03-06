#!/usr/bin/python                                                                                                  
# Weather Underground API Driver 
# This class handles all interactions with the Weather Underground API
import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header

import urllib
import json
import time

Mysql = MVC.loadDriver('Mysql')

class DriverWeatherUnderAPI( object ):
  def __init__( self ):
      Settings     = MVC.loadHelper('Settings')
      self.apikey  = Settings.get_option( 'weatherunderground-apikey' )
      self.zipcode = Settings.get_option( 'weatherunderground-zipcode' )

  def run(self, ):
    api_data = self.fetch()
    results  = {
      'temp_f'      : api_data['current_observation']['temp_f'], 
      'temp_f_feel' : api_data['current_observation']['feelslike_f'],
      'humidity'    : api_data['current_observation']['relative_humidity'].replace( '%', '' )
    }

    return results

  def fetch(self):
    if( self.apikey == '' or self.zipcode == '' ):
      print 'ERROR: Weather Underground requires a zipcode and apikey! '
      return
    url = "http://api.wunderground.com/api/%s/conditions/q/%s.json" % ( self.apikey, self.zipcode )
    response = urllib.urlopen(url);
    data = json.loads(response.read())
    return data

  def save( self, api_data ):
    info = {
      'temp_f'   : api_data['current_observation']['temp_f'],
      'feel_f'   : api_data['current_observation']['feelslike_f'],
      'humidity' : api_data['current_observation']['relative_humidity'].replace( '%', '' ),
      'date'     : time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    Mysql.insert( 'weather_outdoor', info )

# End File: driver/DriverWeatherUnderAPI.py