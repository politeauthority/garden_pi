#!/usr/bin/python
# Installer
# This will have to be run as root, as we will be installing all our dependancies here                                   
import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header
import subprocess

# Install all the software were gonna need to run properly
subprocess.call( "apt-get install arduino",         shell=True )
subprocess.call( "apt-get install python-serial",   shell=True )

subprocess.call( "apt-get install python-cherrypy", shell=True )
subprocess.call( "apt-get install python-jinja2",   shell=True )
subprocess.call( "apt-get install python-dev",      shell=True )

subprocess.call( "apt-get install python-cherrypy", shell=True )

if MVC.raspberry_pi:
    subprocess.call( "apt-get install python-rpi.gpio", shell=True )


# Create the SQL tables we require

Mysql = MVC.loadDriver('Mysql')


# Base Website tables
createTable_options = """CREATE TABLE `"""+ MVC.db['name'] +"""`.`options` (
  `id` 					int(9) NOT NULL AUTO_INCREMENT,
  `meta_key` 		varchar(200) NOT NULL,
  `meta_value` 	varchar(200) NOT NULL,
  `parent`    	int(10) DEFAULT 0,
  `pretty_name` varchar(250) DEFAULT NULL,
  `help_text` 	varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
); """

# createTable_devices = """CREATE TABLE `"""+ MVC.db['name'] +"""`.`devices` (
#   `id` 					id(9) NOT NULL AUTO_INCREMENT,
#   `name` 				varchar(200) NOT NULL,
#   `status_bit`	int(1) NOT NULL,
#   `outlet_num` 	int(10) DEFAULT NULL,
#   `type` 				varchar(250) DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ); """


# User tables
createTable_users  = """CREATE TABLE `"""+ MVC.db['name'] +"""`.`users` (
  `id` 					int(9)       NOT NULL AUTO_INCREMENT,
  `user` 				varchar(100) NOT NULL,
  `email` 			varchar(250) NOT NULL,
  `pass` 				varchar(250) NOT NULL,
  `last_login` 	varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
);"""

createTable_usermeta = """CREATE TABLE `"""+ MVC.db['name'] +"""`.`usermeta` (
  `id` 					int(9) NOT NULL AUTO_INCREMENT,
  `user_id` 		int(10) NOT NULL,
  `parent` 			int(10) NOT NULL,
  `meta_key` 		varchar(200) NOT NULL,
  `meta_value` 	varchar(200) NOT NULL,
  `pretty_name` varchar(250) DEFAULT NULL,
  `help_text`		varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
); """

createTable_user_acl_permissions = """CREATE TABLE `"""+ MVC.db['name'] +"""`.`acl_permissions` (
  `id` 				bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `permKey` 	varchar(30) NOT NULL,
  `permName` 	varchar(30) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `permKey` (`permKey`)
); """

createTable_user_acl_role_perms  = """CREATE TABLE `"""+ MVC.db['name'] +"""`.`acl_role_perms` (
  `id` 			bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `roleID`	bigint(20) NOT NULL,
  `permID` 	bigint(20) NOT NULL,
  `value` 	tinyint(1) NOT NULL DEFAULT '0',
  `addDate` datetime NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `roleID_2` (`roleID`,`permID`)
); """

createTable_user_acl_roles       = """CREATE TABLE `"""+ MVC.db['name'] +"""`.`acl_roles` (
  `id` 				int(10) unsigned NOT NULL AUTO_INCREMENT,
  `roleName`	varchar(20) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `roleName` (`roleName`)
); """

createTable_user_acl_user_perms  = """CREATE TABLE `"""+ MVC.db['name'] +"""`.`acl_user_perms` (
  `id` 			    bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `userID`	    bigint(20) NOT NULL,
  `permID` 	    bigint(20) NOT NULL,
  `value` 	    tinyint(1) NOT NULL DEFAULT '0',
  `addDate` datetime NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `userID` (`userID`,`permID`)
 ); """

createTable_user_acl_user_roles  = """CREATE TABLE `"""+ MVC.db['name'] +"""`.`acl_user_roles` (
  `userID`      bigint(20) NOT NULL,
  `roleID`      bigint(20) NOT NULL,
  `addDate`     datetime NOT NULL,
  UNIQUE KEY `userID` (`userID`,`roleID`)
); """


# Sensor reading tables
createTable_weather = """CREATE TABLE `"""+ MVC.db['name'] +"""`.`weather` (
	`id` 										int(9) NOT NULL AUTO_INCREMENT,
  `date`                  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`indoor_temp_f` 				varchar(10) DEFAULT NULL,
  `indoor_humidity` 			varchar(50) DEFAULT NULL,
  `outdoor_temp_f` 				varchar(50) DEFAULT NULL,
  `outdoor_temp_f_feels`	varchar(50) DEFAULT NULL,
  `outdoor_humidity` 			varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
);"""

createTable_wate = """CREATE TABLE `"""+ MVC.db['name'] +"""`.`water` (
  `id`            int(11) NOT NULL AUTO_INCREMENT,
  `date`          timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `water_temp_1`  decimal(4,2) DEFAULT NULL,
  `flow_rate_1`   decimal(4,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
); """

# @todo: make a backup of the db if somethings there
Mysql.ex( "DROP DATABASE IF EXISTS `%s`;" % MVC.db['name'] )
Mysql.ex( "CREATE DATABASE IF NOT EXISTS `%s`;" % MVC.db['name'] )
Mysql.ex( 'DROP TABLE IF EXISTS %s.options' % MVC.db['name']  )
Mysql.ex( createTable_options )
# Mysql('DROP TABLE IF EXISTS %s.devices' % MVC.db['name']  )
# Mysql.ex( createTable_devices )
Mysql.ex( 'DROP TABLE IF EXISTS %s.users' % MVC.db['name']  )
Mysql.ex( createTable_users )
Mysql.ex( 'DROP TABLE IF EXISTS %s.usermeta' % MVC.db['name']  )
Mysql.ex( createTable_usermeta )
Mysql.ex( 'DROP TABLE IF EXISTS %s.acl_permissions' % MVC.db['name']  )
Mysql.ex( createTable_user_acl_permissions )
Mysql.ex( 'DROP TABLE IF EXISTS %s.acl_role_perms' % MVC.db['name']  )
Mysql.ex( createTable_user_acl_role_perms )
Mysql.ex( 'DROP TABLE IF EXISTS %s.acl_roles' % MVC.db['name']  )
Mysql.ex( createTable_user_acl_roles )
Mysql.ex( 'DROP TABLE IF EXISTS %s.acl_user_perms' % MVC.db['name']  )
Mysql.ex( createTable_user_acl_user_perms )
Mysql.ex( 'DROP TABLE IF EXISTS %s.acl_user_roles' % MVC.db['name']  )
Mysql.ex( createTable_user_acl_user_roles )
Mysql.ex( 'DROP TABLE IF EXISTS %s.weather' % MVC.db['name']  )
Mysql.ex( createTable_weather )
Mysql.ex( 'DROP TABLE IF EXISTS %s.water' % MVC.db['name']  )
Mysql.ex( createTable_water )

Settings = MVC.loadHelper('Settings')

opt_site_url                       = Settings.insert( 'site-url',                        '',      'Site Url',                     '',                                     )
opt_use_sensor_shtx                = Settings.insert( 'use-sensor-shtx',                 '0',     'SHT1x Sensor',                 'Use the temperature humidity sensor'   )

opt_use_network_weatherunderground = Settings.insert( 'use-network-weatherunderground',  '0',     'Weather Underground system',      'Weather Unground System'            )
Settings.insert( 'weatherunderground-apikey',       '',      'Weather Underground API key',  '',                    opt_use_network_weatherunderground[0]  )
Settings.insert( 'weatherunderground-zipcode',      '',      'Weather Underground: Zipcode', '',                    opt_use_network_weatherunderground[0]  )

opt_use_alert                      = Settings.insert( 'use-alert',                       '0',     'Alert System',                 'Use the Alert System'                  )
Settings.insert( 'alert-opt-temp-high',             '85',    'High Temperature Alert',       '',                    opt_use_alert[0]                                      )
Settings.insert( 'alert-opt-temp-low',              '60',    'Low Temperature Alert',        '',                    opt_use_alert[0]                                      )

opt_use_lighttiming                = Settings.insert( 'use-lighttiming',                    '0',  'Light Timing',                 'Use the Light Timing system'           )
Settings.insert( 'lighttiming-start',               '',      'Start Lights',                '',                    opt_use_lighttiming[0]                                 )
Settings.insert( 'lighttiming-stop',                '',      'Stop Lights',                 '',                    opt_use_lighttiming[0]                                 )

opt_prowl                          = Settings.insert( 'use-prowl',                          '',   'Prowl Notifications',          ''                                      )

UserModel  = MVC.loadModel('User')
adminUser = UserModel.create( 'admin', '', 'password' )

#End File: install/install.py