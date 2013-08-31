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
    self.table_name = 'options'

  def get_option( self, meta_key, bool = False ):
    options = Mysql.ex( "SELECT * FROM %s.%s WHERE meta_key = '%s';" % ( MVC.db['name'], self.table_name, meta_key ) )
    try:
      options[0]
    except Exception:
      return False

    if bool:
      if options[0] == '1':
        return True
      elif options[0] == '0':
        return False
    else:
      return options[0][2]

  def get_options( self ):
    options = Mysql.ex( "SELECT * FROM %s.%s ORDER BY `meta_key`;" % ( MVC.db['name'], self.table_name ) )
    return options
  
  def update( self, meta_key, meta_value ):
    value_check = Mysql.ex( "SELECT * FROM %s.%s WHERE meta_key = '%s' " %
     ( MVC.db['name'], self.table_name, meta_key ) );
    if value_check:
      sql = "UPDATE %s.%s SET meta_value = '%s' WHERE meta_key = '%s';" % ( MVC.db['name'], self.table_name, meta_value, meta_key ) 
    else:
      sql = "INSERT INTO %s.%s ( meta_key, meta_value ) VALUES ( '%s', '%s' );" % (  MVC.db['name'], self.table_name, meta_key, meta_value )
    return Mysql.ex( sql )

  # Bulk is dictionary
  def bulk_update( self, bulk ):
    for meta_key, meta_value in bulk.items():
      meta_key = meta_key.replace("settings['", '').replace("']", '')
      self.update( meta_key, meta_value )

  def insert( self, meta_key, meta_value, pretty_name, help_text, parent = 0 ):
    option = {
      'meta_key'    : meta_key,
      'meta_value'  : meta_value,
      'pretty_name' : pretty_name,
      'help_text'   : help_text,
      'parent'      : parent
    }
    Mysql.insert( self.table_name, option )
    return self.get_option( meta_key )

# End File: helpers/HelperSettings.py