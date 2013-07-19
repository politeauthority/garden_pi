#!/usr/bin/python
# This is the GPIO class wrapper for unified communication with the GPIO chipset
import sys
from sys import path
import os

class MVC( object ):

    def __init__( self ):
        self.garden_dir = os.path.abspath( os.path.dirname(__file__) ) + '/'

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

