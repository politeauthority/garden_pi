import sys
from sys import path
import os
import cherrypy
import time

path.insert( 0, 'drivers')
path.insert( 0, 'config')
from DriverMysql import DriverMysql
from DriverGPIO import DriverGPIO

from webserver_config import settings

mysql = DriverMysql()
gpio = DriverGPIO()
cherrypy.config.update( settings )

class Root:
    def index( self ):
        #pump_on = gpio.pump_toggle()
        #print 'The current state of pin 18 is : %s' % str( GPIO.input( led ) )
        
        source  = 'blank';
        return source
    index.exposed = True

    def pump( self  ):
        gpio.pump_toggle()
        return 'this is a different page'
    pump.exposed = True

root = Root()
root.pump = root.pump()



cherrypy.quickstart(Root())
