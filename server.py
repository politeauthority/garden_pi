#!/usr/bin/python
                                                                                                 
# Main Web Server application file  
# 

import sys
import os

from MVC import MVC
MVC = MVC()
# End file header                                                               

from sys import path
import cherrypy
from jinja2 import Environment, FileSystemLoader

path.insert( 1, 'config')
from webserver_config import settings
#from app_config import app_settings
#cherrypy.config.update( settings )


Gpio  = MVC.loadDriver( 'GPIO' )
Weather = MVC.loadModel( 'Weather' )

env = Environment( loader=FileSystemLoader('views') )

class Root:
    
    def index( self ):
        weather = Weather.get_current_indoor()
        #print Weather.get_stats_indoor()
        view = env.get_template('index.html')
        return view.render( salutation='eat it', target=weather )
    index.exposed = True

    def pump( self ):
        Gpio.pump_toggle()
        return 'this is a different page'
    pump.exposed = True

    def foo( self ):
        return 'Foo!'
    foo.exposed = True

root = Root()
root.pump = Root().pump()
root.foo = Root().foo


#cherrypy.tree.mount( Root(), config = settings )
cherrypy.quickstart(  Root(),  config = settings )
# End File: server.py
