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


subprocess.call( "apt-get install arduino",    shell=True )
subprocess.call( "apt-get install python-serial",   shell=True )

subprocess.call( "apt-get install python-cherrypy", shell=True )
subprocess.call( "apt-get install python-jinja2",   shell=True )
subprocess.call( "apt-get install python-dev",      shell=True )

subprocess.call( "apt-get install python-cherrypy", shell=True )

if MVC.raspberry_pi:
    subprocess.call( "apt-get install python-rpi.gpio", shell=True )



subprocess.call( "mysql -h%s -u%s -p%s garden < %s" % ( MVC.db['host'], MVC.db['user'], MVC.db['pass'], MVC.garden_dir + 'install/garden.sql' ), shell=True )
subprocess.call( "mysql -h%s -u%s -p%s garden < %s" % ( MVC.db['host'], MVC.db['user'], MVC.db['pass'], MVC.garden_dir + 'install/garden_options.sql' ), shell=True )
