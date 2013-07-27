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
    weather = Weather.get_current_indoor()
    view = env.get_template('index.html')
    return view.render( d = weather )
  index.exposed = True

  def dashboard( self ):
    Weather = MVC.loadModel('Weather')
    tpl_args = {
      'weather_indoor' : Weather.get_current_indoor()
    }
    view = env.get_template('index.html')
    return view.render( d = tpl_args )
  dashboard.exposed = True

  def weather( self ):
    Weather = MVC.loadModel('Weather')
    tpl_args = {
      'weather_current_indoor' : Weather.get_current_indoor(),
      'weather_min_max'        : Weather.get_min_max(),
      'weather_current_outdoor': Weather.get_current_outdoor(),
    }
    view = env.get_template('weather.html')
    return view.render( d = tpl_args )
  weather.exposed = True

  def chart( self ):
    Weather = MVC.loadModel('Weather')
    tpl_args = {
      'weather_stats_indoor'   : Weather.get_stats_indoor( 86400 ),
      'weather_stats_outdoor'  : Weather.get_stats_chart( 86400 ),
    }
    view = env.get_template('chart.html')
    return view.render( d = tpl_args )
  chart.exposed = True

  def users( self ):
    view = env.get_template('users.html')
    return view.render()
  users.exposed = True

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

  def form( self, *request):
    print request
    return request
  form.exposed = True

  def test( self ):
    Weather = MVC.loadModel('Weather')
    return str( Weather.get_stats_chart() )
  test.exposed = True


root = Root()
root.dashboard     = Root().dashboard()
root.weather       = Root().weather()
root.chart         = Root().chart()
root.settings      = Root().settings()
root.users         = Root().users()
root.form          = Root().form()
root.test          = Root().test()
cherrypy.quickstart(  Root(),  config = settings )

# End File: server.py
