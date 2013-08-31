#!/usr/bin/python                                                                                                
# User Model
# This model controls interactions with the indoor and outdoor weather actions which need to occur
import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header
Mysql    = MVC.loadDriver('Mysql')
Settings = MVC.loadHelper('Settings')

class ModelUser( object ):

  def __init__( self ):
    self.db_name = MVC.db['name']


  def getByName( self, user_name ):
    sql = 'SELECT * FROM `%s`.`users` WHERE `user` = "%s" LIMIT 1;' % ( MVC.db['name'], user_name )
    user = Mysql.ex( sql )
    return user

  def getAll( self ):
    sql = 'SELECT * FROM `%s`.`users`;' % self.db_name
    users = Mysql.ex( sql )
    return users
    
  def create( self, user_name, email, password ):
    data = {
      'user'  : user_name,
      'email' : email,
      'pass'  : password,
    }
    # @todo: check user name space
    # @todo: hash passwords dummy
    Mysql.insert( 'users', data )
    return self.getByName( user_name )

  def addMeta( self, user_id, meta_key, meta_value, pretty_name, help_text, parent  ):
    data = {
      'user_id'     : user_id,
      'meta_key'    : meta_key,
      'meta_value'  : meta_value,
      'pretty_name' : pretty_name,
      'help_text'   : help_text,
      'parent'      : parent,
    }
    Mysql.insert( 'usermeta', data )

# End File: models/ModelUser.py
