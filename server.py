import sys
from sys import path
import os
import cherrypy
import webserver_config
import RPi.GPIO as GPIO
import time

path.insert( 0, 'drivers')
from DriverMysql import DriverMysql
from DriverGPIO import DriverGPIO

mysql = DriverMysql()
gpio = DriverGPIO()
cherrypy.config.update( webserver_config.settings )

class Root:
    def index( self ):
        pump_on = gpio.pump_toggle()
        #print 'The current state of pin 18 is : %s' % str( GPIO.input( led ) )
        return pump_on
    index.exposed = True

    def pump( self  ):
        GPIO.setmode(GPIO.BCM)
        led = 18
        GPIO.setup(led, GPIO.OUT)
        GPIO.output( led, False )        
        return 'this is a different page'
    pump.exposed = True

root = Root()
root.pump = root.pump()



cherrypy.quickstart(Root())
