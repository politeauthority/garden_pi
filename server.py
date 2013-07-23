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

  def weather( self, *args ):
    Weather = MVC.loadModel('Weather')
    if args and args[0] == 'chart':
      tpl_args = {
        'weather_current_indoor' : Weather.get_current_indoor(),
        'weather_stats_indoor'   : Weather.get_stats_indoor()
        }
    else:
      tpl_args = {
        'weather_current_indoor' : Weather.get_current_indoor(),
        'weather_stats_indoor'   : Weather.get_stats_indoor(),
        'weather_min_max'        : Weather.get_min_max(),
        'weather_current_outdoor': Weather.get_current_outdoor(),
      }
    view = env.get_template('weather.html')
    return view.render( d = tpl_args )
  weather.exposed = True

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


root = Root()
root.weather   = Root().weather()
root.dashboard = Root().dashboard()
root.settings  = Root().settings()
root.users     = Root().users()
root.form      = Root().form()
cherrypy.quickstart(  Root(),  config = settings )

# End File: server.py
