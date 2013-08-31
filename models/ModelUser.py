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

	def getByName( user_name ):
		sql = 'SELECT * FROM %s.users WHERE `user` = "%s LIMIT 1";' % user_name
		user = Mysql.ex( sql )
		return user[0]

  def create( self, user_name, email, pass ):
  	data = {
  		'user'  : user_name,
  		'email' : email,
  		'pass'  : pass,
  	}
  	Mysql.insert( 'users', data )
  	return self.getByName( user_name )

  def addMeta( user_id, meta_key, meta_value, pretty_name, help_text, parent  ):
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
