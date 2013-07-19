#!/usr/bin/python                                                                                                  
# Settings Helper
# @description
# This class aids managing settings in a meta-key / meta-value way
# @requirements ( drivers/DriverMySql )

import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header


Mysql = MVC.loadDriver('Mysql')

class HelperSettings( object ):

  def __init__( self ):
    self.table_name = 'garden_options'

  def update( self, meta_key, meta_value ):
    value_check = Mysql.ex( "SELECT * FROM %s.%s WHERE meta_key = '%s' " %
     ( MVC.db['name'], self.table_name, meta_key ) );
    if value_check:
      sql = "UPDATE %s.%s SET meta_value = '%s' WHERE meta_key = '%s';" % ( MVC.db['name'], self.table_name, meta_value, meta_key ) 
    else:
      sql = "INSERT INTO %s.%s ( meta_key, meta_value ) VALUES ( '%s', '%s' );" % (  MVC.db['name'], self.table_name, meta_key, meta_value )
    return Mysql.ex( sql )

  def get_options( self ):
    options = Mysql.ex( "SELECT * FROM %s.%s;" % ( MVC.db['name'], self.table_name ) )
    return options

# End File: helpers/HelperSettings.py
