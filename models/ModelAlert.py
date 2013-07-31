#!/usr/bin/python                                                                                                
# Alert Model
# This model controls interactions with the indoor and outdoor weather actions which need to occur
import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header

Settings = MVC.loadHelper('Settings')

class ModelAlert( object ):
  def __init__( self ):
    
    self.temp_high = Settings.get_option('alert-opt-temp-high')
    self.temp_low  = Settings.get_option('alert-opt-temp-low')

  def messaging( self, message ):
    if Settings.get_option('use-prowl'):
      Prowl = MVC.loadDriver('Prowl')
      prowl_api_key = Settings.get_option('prowl-apikey')

      Prowl.send( prowl_api_key, message[0], message[1], 1 )

# End File: models/ModelAlert.py