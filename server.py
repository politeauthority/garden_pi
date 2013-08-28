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

env = Environment( loader=FileSystemLoader('views') )

class Root:
    
  def index( self ):
    Weather = MVC.loadModel('Weather')
    weather = Weather.get_current()
    view = env.get_template('index.html')
    return view.render( d = weather )
  index.exposed = True

  def dashboard( self ):
    Weather = MVC.loadModel('Weather')
    tpl_args = {
      'weather_indoor' : Weather.get_current()
    }
    view = env.get_template('index.html')
    return view.render( d = tpl_args )
  dashboard.exposed = True


  #Weather Pages

  def weather( self ):
    Weather = MVC.loadModel('Weather')
    tpl_args = {
      'weather_current' : Weather.get_current(),
      'weather_min_max' : Weather.get_min_max(),
    }
    view = env.get_template('weather/index.html')
    return view.render( d = tpl_args )
  weather.exposed = True

  def chart_humidity( self ):
    Weather = MVC.loadModel('Weather')
    tpl_args = {
      'weather_stats'   : Weather.get_stats( )
    }
    view = env.get_template('weather/chart-humidity.html')
    return view.render( d = tpl_args )
  chart_humidity.exposed = True

  def chart_temp( self ):
    Weather = MVC.loadModel('Weather')
    tpl_args = {
      'weather_stats'   : Weather.get_stats( )
    }
    view = env.get_template('weather/chart-temp.html')
    return view.render( d = tpl_args )
  chart_temp.exposed = True


  #Water Pages

  def water( self ):
    test = 'something'
    view = env.get_template('water.html')    
    return view.render( )
  water.exposed = True


  #Settings Pages

  def settings( self, *boom ):
    Weather  = MVC.loadModel('Weather')
    Settings = MVC.loadHelper( 'Settings' )
    #Settings.update( 'url', 'http://www.somewhere.com' )
    tpl_args = {
      'settings'     : Settings.get_options()
    }
    view = env.get_template('settings.html')
    return view.render( d = tpl_args )
  settings.exposed = True

  def settings_update( self, *args, **kwargs ):
    if kwargs:
      Settings = MVC.loadHelper( 'Settings' )
      Settings.bulk_update( kwargs )
    cherrypy.InternalRedirect('/')
  settings_update.exposed = True

  def settings_users( self ):
    view = env.get_template('users.html')
    return view.render()
  settings_users.exposed = True

root = Root()
root.dashboard        = Root().dashboard()
root.weather          = Root().weather()
root.chart_temp       = Root().chart_temp()
root.chart_humidity   = Root().chart_humidity()
root.water            = Root().water()
root.settings         = Root().settings()
root.settings_update  = Root().settings_update()
root.settings_users   = Root().settings_users()

cherrypy.quickstart(  Root(),  config = MVC.cherrypy_config )

# End File: server.py
