#!/usr/bin/python                                                                                                  
# ACL Helper
# @description
#   Access Control List manager 
# @requirements ( drivers/DriverMySql )

import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header


Mysql = MVC.loadDriver('Mysql')

class HelperACL( object ):

  def __init__( self ):
    self.perms      = []
    self.user_id    = '';
    self.user_roles = '1';
    self.database   = MVC.db['name'] 
  
  def getUserRoles( self ):
    sql = "SELECT * FROM %s.acl_user_roles WHERE user_id = %s ORDER BY `addDate` ASC" % ( self.database, self.user_id )

# End File: helpers/HelperACL.py
