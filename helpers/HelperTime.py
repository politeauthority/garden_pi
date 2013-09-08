#!/usr/bin/python
# Time Helper
# @description
# Class handling basic time calculations.
#

import sys
import os

sys.path.append( os.path.join(os.path.dirname(__file__), '..', '') )
from MVC import MVC
MVC = MVC()
# End file header

from datetime import date, datetime, time, timedelta

class HelperTime( object ):

	def now( self ):
		return datetime.now()

# End File: helpers/HelperTime.py