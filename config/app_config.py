#Web Server Config FIle

import cherrypy

app_settings = { 
    '/': {
        'request.dispatch'     : cherrypy.dispatch.MethodDispatcher(),
        #'favicon_ico'          : 'favicon.ico',
        'tools.staticdir.root' : "/home/pi/garden_pi/public_html/",
        'tools.staticdir.debug': True,
    },
    '/css': {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir': "css"
    },
    '/style.css':{
        'tools.staticfile.on' : True,
        'tools.staticfile.filename' : "/home/pi/garden_pi/public_html/css/default.css"
    },
    '/js': {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir': "js"
    }
}
