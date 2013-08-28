#!/usr/bin/python
# Formula Helper
# @description
# Class for all those conversions that need to be made
#

import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header

from os import path

class HelperFormula( object ):

  def celcius_to_fahrenheit( self, celcius ):
    return round( ( ( celcius * 9 ) / 5 ) + 32, 1 ) 

        
# End File: helpers/HelperFormula.py
