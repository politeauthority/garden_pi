#Web Server Config FIle

import os
import string
import cherrypy

settings = { 
 'global': {
    'server.socket_port' : 8099,
    'server.socket_host': "10.1.10.69",
    'server.socket_file': "",
    'server.socket_queue_size': 5,
    'server.protocol_version': "HTTP/1.0",
    'server.log_to_screen': True,
    'server.log_file': "",
    'server.reverse_dns': False,
    'server.thread_pool': 40,
    'server.environment': "development",
#    'tools.mako.directories' : [os.path.join(root_dir,'templates')],
 },
'/': {
 'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
},
 '/css/default.css': {
    'static_filter.on': True,
    'static_filter.file': "data/css/default.css"
 }
}
