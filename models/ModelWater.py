#!/usr/bin/python                                                                                                
# Water Model
# This model controls interactions with the water database interactions
import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header

import time
Mysql = MVC.loadDriver('Mysql')

class ModelWater( object ):

  def store_info( self, temp_1 ):
    info = {
      'water_temp_1'        : temp_1
    }
    Mysql.insert( 'water', info )

# End File: models/ModelWater.py