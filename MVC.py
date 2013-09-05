#!/usr/bin/python
# Model View Controller Class
# A relativly simple class to help connect and unify the Garden Pi web and hardware aspects

import sys
from sys import path
import os

from config.webserver_config import settings as cherrypy_config
from config.config import settings as garden_pi_config

class MVC( object ):

  def __init__( self ):
    self.garden_dir   = os.path.abspath( os.path.dirname(__file__) ) + '/'
    self.logging      = True
    self.raspberry_pi = True
    self.db           = {
      'host' : garden_pi_config['database']['host'],
      'name' : garden_pi_config['database']['name'],
      'user' : garden_pi_config['database']['user'],
      'pass' : garden_pi_config['database']['pass']
    }

    cherrypy_config['global']['server.sock_port'] = 8787
    cherrypy_config['global']['server.sock_host'] = "10.1.10.68"
    self.cherrypy_config = cherrypy_config
    #self.cherrypy_config['global']['server.sock_port'] = '10.1.10.68'
    #self.cherrypy_config['global']['server.sock_host'] = 8787

    #self.cherrypy_config['global']['server.sock_port'] = garden_pi_config['webserver']['host_port']
    #self.cherrypy_config['global']['server.sock_host'] = garden_pi_config['webserver']['host_ip']
    self.cherrypy_config['/']['tools.staticdir.root']  = '%spublic_html' % self.garden_dir

  def loadDriver( self, driver_name, build_var =  False ):
    return self.loadObject( 'Driver', driver_name, build_var )

  def loadModel( self, model_name, build_var =  False ):
    return self.loadObject( 'Model', model_name, build_var )

  def loadHelper( self, helper_name, build_var = False ):
    return self.loadObject( 'Helper', helper_name, build_var )

  def loadObject( self, obj_type, obj_name, build_var ):
    path.insert( 1, self.garden_dir + obj_type.lower() + "s" )
    obj_name = obj_type + obj_name
    __import__( obj_name )
    if build_var:
      obj = getattr( sys.modules[ "%s" % obj_name ], "%s" % obj_name )( build_var )
    else:
      obj = getattr( sys.modules[ "%s" % obj_name ], "%s" % obj_name )()
    return obj

# Endfile: MVC.py
