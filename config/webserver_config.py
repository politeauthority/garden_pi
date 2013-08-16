#Web Server Config File

import os
import string
import cherrypy

settings = { 
    'global': {
        'server.socket_port'       : 8099,
        'server.socket_host'       : "10.1.10.68",
        'server.socket_file'       : "",
        'server.socket_queue_size' : 5,
        'server.protocol_version'  : "HTTP/1.0",
        'server.log_to_screen'     : True,
        'server.log_file'          : "log/server.log",
        'server.reverse_dns'       : False,
        'server.thread_pool'       : 40,
        'server.environment'       : "development",
    },
    '/': {
        #'request.dispatch'     : cherrypy.dispatch.MethodDispatcher(),
        #'favicon_ico'          : 'favicon.ico',
        'tools.staticdir.root' : "/home/pi/garden_pi/public_html/",
        'tools.staticdir.debug': True,
    },
    '/css': {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir': "css"
    },
    '/js': {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir': "js"
    },
    '/libs': {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir': "libs"
    }
}

# End file: config/webserver_config.py