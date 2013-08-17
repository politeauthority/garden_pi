#!/usr/bin/python
# Model View Controller Class
# A relativly simple class to help connect and unify the Garden Pi web and hardware aspects

import sys
from sys import path
import os

from config.webserver_config import settings as cherrypy_config
from config.primary_config import settings as garden_pi_config

class MVC( object ):

  def __init__( self ):
    self.garden_dir   = os.path.abspath( os.path.dirname(__file__) ) + '/'
    self.logging      = True
    self.raspberry_pi = True
    self.db           = {
      'host' : garden_pi_config['database']['host'],
      'name' : 'garden',
      'user' : 'root',
      'pass' : 'cleancut',
    }

    self.cherrypy_config = cherrypy_config
    self.cherrypy_config['global']['server.sock_port'] = garden_pi_config['webserver']['host_port']
    self.cherrypy_config['global']['server.sock_host'] = garden_pi_config['webserver']['host_ip']
    self.cherrypy_config['/']['tools.staticdir.root']  = '%spublic_html' % self.garden_dir

  def loadDriver( self, driver_name ):
    path.insert( 1, self.garden_dir + 'drivers' )
    driver_name = 'Driver' + driver_name
    __import__( driver_name )
    driver = getattr( sys.modules[ "%s" % driver_name ], "%s" % driver_name )()
    return driver

  def loadModel( self, model_name ):
    path.insert( 1, self.garden_dir + 'models')
    model_name = 'Model' + model_name
    __import__( model_name )
    model = getattr( sys.modules[ "%s" % model_name ], "%s" % model_name )()
    return model

  def loadHelper( self, helper_name ):
    path.insert( 1, self.garden_dir + 'helpers')
    helper_name = 'Helper' + helper_name
    __import__( helper_name )
    helper = getattr( sys.modules[ "%s" % helper_name ], "%s" % helper_name )()
    return helper

# Endfile: MVC.py
