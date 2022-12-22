import datetime
# import mysql.connector
import pymysql
__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = pymysql.connect(user='root', password='Eqpo0218@anu', host='localhost',database='gs')

  return __cnx

# get_sql_connection()
