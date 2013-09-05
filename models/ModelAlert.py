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
      self.prowl_alerts( message )
    return True

  def prowl_alerts( self, message ):
    UserModel = MVC.loadModel( 'User' )
    users = UserModel.getUsersWithMeta( 'prowl-apikey' )
    Prowl = MVC.loadDriver('Prowl')
    for user in users:
      Prowl.send( user['meta']['prowl-apikey'], message[0], message[1], 1 )

# End File: models/ModelAlert.py