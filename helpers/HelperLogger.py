#!/usr/bin/python
# Logger Helper
# @description
# Class for logging anything we may want to write to logs
#

import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header


class HelperLogger( object ):

  def __init__( self ):
    self.log_dir = MVC.garden_dir + 'logs/'
    self.logging = MVC.logging

  def write( self, title, message, log_file = None):
    from datetime import date, datetime, time, timedelta
    
    if self.logging:
      if log_file == None:
        log_file = 'main.log'
      else:
        log_file = log_file + '.log'
      message = message + "\n"
      f = open( self.log_dir + log_file,'a')
      f.write('[%s] %s: %s' % (  datetime.now(), title, message ) )
        
# End File: helpers/HelperLogger.py
