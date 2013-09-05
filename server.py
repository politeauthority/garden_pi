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
    view = env.get_template('water/index.html')
    tpl_args = {}
    return view.render( d = tpl_args )
  water.exposed = True

  def chart_water_temp( self ):
    WaterModel = MVC.loadModel('Water')
    tpl_args = {
      'water_stats'   : WaterModel.get_stats( )
    }
    view = env.get_template('water/chart-temp.html')
    return view.render( d = tpl_args )
  chart_water_temp.exposed = True


  #Settings Pages

  def settings( self, *boom ):
    UsersModel = MVC.loadModel('User')
    Settings   = MVC.loadHelper( 'Settings' )
    #Settings.update( 'url', 'http://www.somewhere.com' )
    tpl_args = {
      'users'        : UsersModel.getAll(),
      'settings'     : Settings.get_options()
    }
    view = env.get_template('settings/index.html')
    return view.render( d = tpl_args )
  settings.exposed = True

  def settings_update( self, *args, **kwargs ):
    if kwargs:
      Settings = MVC.loadHelper( 'Settings' )
      Settings.bulk_update( kwargs )
    cherrypy.InternalRedirect('/')
  settings_update.exposed = True

  def settings_user_add( self ):
    view = env.get_template('settings/user_add.html')
    return view.render()
  settings_user_add.exposed = True

root = Root()
root.dashboard           = Root().dashboard()
root.weather             = Root().weather()
root.chart_temp          = Root().chart_temp()
root.chart_humidity      = Root().chart_humidity()
root.water               = Root().water()
root.chart_water_temp    = Root().chart_water_temp()
root.settings            = Root().settings()
root.settings_update     = Root().settings_update()
root.settings_user_add   = Root().settings_user_add()
cherrypy.quickstart(  Root(),  config = MVC.cherrypy_config )

# End File: server.py
