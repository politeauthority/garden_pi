#!/usr/bin/python
import MySQLdb as mdb

class DriverMysql( object ):
  def __init__( self ):
    self.host     = 'localhost'
    self.dbname   = 'garden'
    self.user     = 'root'
    self.password = 'cleancut'

  def ex(self, query):
    conn = mdb.connect( self.host, self.user, self.password)
    cur = conn.cursor()
    cur.execute( query )
    return cur.fetchall()

  def insert(self, table, items ):
    columns = []
    values = []
    for column, value in items.items():
      columns.append(column)
      values.append( str(value) )
    column_sql = ','.join( columns )
    value_sql = ''
    for value in values:
        value_sql = value_sql + '"%s",' % self.escape_string( value )
    value_sql = value_sql.rstrip( value_sql[-1:])
    sql = "INSERT INTO %s.%s (%s) VALUES(%s)" % ( self.dbname, table, column_sql, value_sql )
    self.ex( sql )

  def update( self, table, items, where, limit = 1 ):
    set_sql = ''
    for column, value in items.items():
      set_sql = set_sql + '`%s`="%s", ' % ( column, value )
    set_sql = set_sql.rstrip( set_sql[-2:] )
    set_sql = set_sql + ' '
    sql = "UPDATE %s.%s SET %s WHERE `%s` = '%s'" % ( self.dbname, table, set_sql, where[0], where[1] )
    self.ex( sql )

  def escape_string( self, string ):
      return mdb.escape_string( string )

# End File: driver/DriverMysql