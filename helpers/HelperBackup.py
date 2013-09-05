#!/usr/bin/python                                                                                           
# Backup Helper                                                                                             
# @description                                                                                              
# Class for database, logfiles, and remote export of those files if needed                                  
#                                                                                                           

import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header                                                                                           

from os import path
import subprocess

class HelperBackup( object ):

  def __init__( self ):
    self.db_host    = MVC.db['host']
    self.db_name    = MVC.db['name']
    self.db_user    = MVC.db['user']
    self.db_pass    = MVC.db['pass']
    self.backup_dir = MVC.garden_dir + 'backup/'

  def database( self ):
    if path.isdir( self.backup_dir ) == False:
        os.mkdir( self.backup_dir )
    command = "mysqldump -h%s -u%s -p%s %s > %s.sql" % ( self.db_host, self.db_user, self.db_pass, self.db_name, self.backup_dir + 'backup' )
    subprocess.call( command, shell=True )

# End File: helpers/HelperBackup.py
