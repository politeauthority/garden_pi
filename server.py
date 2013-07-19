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

Gpio  = MVC.loadDriver( 'GPIO' )
Weather = MVC.loadModel( 'Weather' )

env = Environment( loader=FileSystemLoader('views') )

class Root:
    
  def index( self ):
    weather = Weather.get_current_indoor()
    view = env.get_template('index.html')
    return view.render( salutation='eat it', target=weather )
  index.exposed = True

  def dashboard( self ):
    view = env.get_template('dashboard.html')
    tpl_args = {
      'weather_indoor' : Weather.get_current_indoor()
    }
    return view.render( data = tpl_args )
  dashboard.exposed = True

  def weather( self ):
    view = env.get_template('weather.html')
    tpl_args = {
      'weather_current_indoor' : Weather.get_current_indoor(),
      'weather_stats_indoor'   : Weather.get_stats_indoor()
    }
    return view.render( d = tpl_args )
  weather.exposed = True

  def settings( self ):
    view = env.get_template('settings.html')
    tpl_args = {
      'weather_current_indoor' : Weather.get_current_indoor(),
      'weather_stats_indoor'   : Weather.get_stats_indoor()
    }
    return view.render( d = tpl_args )
  settings.exposed = True


root = Root()
root.weather   = Root().weather()
root.dashboard = Root().dashboard()
root.settings  = Root().settings()


cherrypy.quickstart(  Root(),  config = settings )

# End File: server.py
