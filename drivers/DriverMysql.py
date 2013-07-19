#!/usr/bin/python
import MySQLdb as mdb

class DriverMysql( object ):
    def __init__( self ):
        self.host     = 'localhost'
        self.user     = 'root'
        self.password = 'cleancut'

    def ex(self, query):
        conn = mdb.connect( self.host, self.user, self.password)
        cur = conn.cursor()
        cur.execute( query )
        return cur.fetchall()

    def escape_string( self, string ):
        return mdb.escape_string( string )
