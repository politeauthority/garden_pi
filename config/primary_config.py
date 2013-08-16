#Primary config file, before install this is the only file you must modify

settings = { 
    'database': {
        'host'       : 'localhost',
        'user'       : 'root',
        'pass'       : 'cleancut',
        'name'       : 'garden',
    },
    'webserver':{
        'host_ip' : "/home/pi/garden_pi/public_html/",
        'host_port': True,
    },
}
