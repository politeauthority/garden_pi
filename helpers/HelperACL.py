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

import types
Mysql = MVC.loadDriver('Mysql')

# TODO: combine this with the getPermNameFromID
# TODO: combine this with the getPermNameFromID 

# TODO: combine userSpecific Perms
# TODO  add more features to help in UI for editing all of this
class HelperACL( object ):

  def __init__( self, user_id = False ):
    self.database   = MVC.db['name'] 
    self.perms      = []
    self.user_id    = user_id
    self.user_roles = self.getUserRoles()
    self.buildACL()

  def hasPerm( self, perm_key ):
    for perm in self.perms:
      if perm['perm'] == perm_key:
        if perm['value'] == 1:
          return True
        else:
          return False
      else:
        return False

  def buildACL( self ):
    if self.user_id:
      if len( self.user_roles ) > 0:
        self.perms = self.getRolePerms( self.user_roles )
    return self.perms
  
  def getUserRoles( self ):
    roles = []
    if self.user_id:
      sql = "SELECT * FROM `%s`.`acl_user_roles` WHERE `userID` = '%s' ORDER BY `addDate` ASC;" % ( self.database, self.user_id )
      results = Mysql.ex( sql )
      for role in results:
        roles.append( role[1] )
    return roles

  # Get the PERMISSIONS assigned to a ROLE
  # @param : role list or string
  def getRolePerms( self, roles ):
    sql = 'SELECT * FROM `%s`.`acl_role_perms` WHERE `roleID` ' % self.database
    if isinstance( roles, types.ListType ):
      role_ids = ''
      for role in roles:
        role_ids += str( role ) + ','
      role_ids = role_ids[:-1]
      sql += 'IN ( %s ) ORDER BY `ID` ASC;' % role_ids
    else:
      sql += 'IN ( %s ) ORDER BY `ID` ASC;' % roles 

    rolePerms = Mysql.ex( sql )

    perms = []
    for rolePerm in rolePerms:
      pK = self.getPermKeyFromID( rolePerm[2] )
      if pK == '':
        continue
      if rolePerm[3] == 1:
        hP = True
      else:
        hP = False
      perm_dict = { 
        'perm'       : pK,
        'inheritted' : False,
        'value'      : hP,
        'name'       : self.getPermNameFromID( rolePerm[2] ),
        'ID'         : rolePerm[0]
      }
      perms.append( perm_dict )
    return perms

  def getUserPerms( self, user_id ):
    sql = "SELECT * FROM `%s`.`acl_user_perms` WHERE `userID` = %s ORDER BY `addDate` ASC;" % ( self.database, user_id )
    userPerms = Mysql.ex( sql )

    perms = []
    for userPerm in userPerms:
      pK = self.getPermKeyFromID( userPerm[2] )
      if pK == '':
        continue      
      if userPerm[3] == 1:
        hP = True
      else:
        hP = False
      perm_dict = { 
        'perm'       : pK,
        'inheritted' : False,
        'value'      : hP,
        'name'       : self.getPermNameFromID( rolePerm[2] ),
        'ID'         : rolePerm[0]
      }
      perms.append( perm_dict )
    return perms

  # TODO: combine this with the getPermNameFromID 
  def getPermKeyFromID( self, perm_id ):
    sql = "SELECT `permKey` FROM `%s`.`acl_permissions` WHERE `ID` = %s;" % ( self.database, perm_id )
    permKeyID = Mysql.ex( sql )
    return permKeyID[0][0]

  # TODO: combine this with the getPermKeyFromID 
  def getPermNameFromID( self, perm_id ):
    sql = "SELECT `permName` FROM `%s`.`acl_permissions` WHERE `ID` = %s;" % ( self.database, perm_id )
    permKeyID = Mysql.ex( sql )
    return permKeyID[0][0]    

  def addUserRole( self, user_id, role_id ):
    Time = MVC.loadHelper('Time')    
    sql = 'INSERT INTO `%s`.`acl_user_roles` ( `userID`, `roleID`, `addDate` ) VALUES ( "%s", "%s", "%s")' % ( self.database, user_id, role_id, Time.now() )
    Mysql.ex( sql )

  def createRole( self, role_name ):
    sql = 'INSERT INTO `%s`.`acl_roles` ( roleName ) VALUES ( "%s" );' % ( self.database, role_name )
    Mysql.ex( sql )

  def createPerm( self, perm_key, perm_name ):
    sql_check = 'SELECT * FROM `%s`.`acl_permissions` WHERE `permKey` = "%s"' % ( self.database, perm_key )
    perm_exists = Mysql.ex( sql_check )
    if len( perm_exists ) == 0:
      sql = 'INSERT INTO `%s`.`acl_permissions` ( permKey, permName ) VALUES ( "%s", "%s" );' % ( self.database, perm_key, perm_name )
      Mysql.ex( sql )

  def createRolePerm( self, role_id, perm_id ):
    Time = MVC.loadHelper('Time')
    sql_check = 'SELECT * FROM `%s`.`acl_role_perms` WHERE `roleID` = "%s" AND `permID` = "%s";' % ( self.database, role_id, perm_id )
    role_perm_exists = Mysql.ex( sql_check )
    if len( role_perm_exists ) == 0:
      insert_sql = 'INSERT INTO `%s`.`acl_role_perms` ( `roleID`, `permID`, `value`, `addDate` ) VALUES( "%s", "%s", "1", "%s");' % ( self.database, role_id, perm_id, Time.now() )
      Mysql.ex( insert_sql )
    else:
      update_sql = "UPDATE `%s`.`acl_role_perms` SET `value` = 1 WHERE ID = %s; " % ( self.database, role_perm_exists[0][0] )
      Mysql.ex( update_sql )

# End File: helpers/HelperACL.py
