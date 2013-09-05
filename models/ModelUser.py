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

  def getById( self, user_id ):
    sql = 'SELECT * FROM `%s`.`users` WHERE `id` = "%s" LIMIT 1;' % ( MVC.db['name'], user_id )
    user = Mysql.ex( sql )
    the_user = {
      'id'         : user[0][0],
      'user'       : user[0][1],
      'last_login' : user[0][4],
      'meta'       : self.getUserMeta( user[0][0] )
    }
    return the_user

  def getAll( self ):
    sql = 'SELECT * FROM `%s`.`users`;' % self.db_name
    users = Mysql.ex( sql )
    return users

  def getUsersWithMeta( self, meta_key ):
    sql = 'SELECT * FROM %s.usermeta WHERE `meta_key` = "%s";' % ( self.db_name, meta_key  )
    meta_records = Mysql.ex( sql )
    users = []
    for meta in meta_records:
      users.append( self.getById( meta[1] ) )
    return users

  def getUserMeta( self, user_id ):
    sql = 'SELECT * FROM `%s`.`usermeta` WHERE `user_id` = "%s" LIMIT 1;' % ( MVC.db['name'], user_id )
    user_meta = Mysql.ex( sql )
    meta_dict = {}
    for meta in user_meta:
      meta_dict[ meta[3] ]= meta[4]
    return meta_dict


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



  def updateUserMeta( self, user_id, meta_key, meta_value ):
    data = {
      'meta_value' : meta_value,
    }
    where = {
      'user_id'  : user_id,
      'meta_key' : meta_key
    }
    Mysql.update( 'usermeta', data, where )

# End File: models/ModelUser.py
