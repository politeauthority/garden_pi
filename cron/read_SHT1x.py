import sys
from sys import path
import os
import time

# Grab the driver files we'll need
sys.path.append( os.path.join(os.path.dirname(__file__), '..', 'drivers') )
from DriverMysql import DriverMysql
from DriverGPIO  import DriverGPIO
Mysql = DriverMysql()
GPIO = DriverGPIO()

sensor = GPIO.read_sht1x()

Mysql.ex("INSERT INTO `garden`.`weather_indoor` (`temp_f`, `humidity`, `date`) VALUES ( '%s', '%s', '%s' )" % ( sensor[1], sensor[2], time.strftime("%Y-%m-%d %H:%M:%S") ) )

print( "Temperature: {} Humidity: {} Dew Point: {}".format( sensor[1], sensor[2], sensor[3] ) )
