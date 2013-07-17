#!/usr/bin/python
                                                                                                 
# Web Server                                                                                  
# 

import sys
import os

from MVC import MVC
MVC = MVC()
# End file header                                                                                

from sys import path
import os
import cherrypy
#import CherrypyMako
import time

#CherrypyMako.setup()
path.insert( 1, 'config')
from webserver_config import settings

Gpio  = MVC.loadDriver( 'GPIO' )
Weather = MVC.loadModel( 'Weather' )

cherrypy.config.update( settings )

class Root:
    def index( self ):
        #pump_on = gpio.pump_toggle()
        #print 'The current state of pin 18 is : %s' % str( GPIO.input( led ) )
        print Weather.get_stats_indoor()
        source  = 'blank';
        return source
    index.exposed = True

    def pump( self  ):
        Gpio.pump_toggle()
        return 'this is a different page'
    pump.exposed = True

root = Root()
root.pump = root.pump()

cherrypy.quickstart(Root())

# End File: server.py
