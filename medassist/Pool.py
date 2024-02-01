import pymysql as sql
from pymysql.cursors import DictCursor

def ConnectionPooling():
      db=sql.connect(host='localhost',port=3306,user='root',passwd='123456',db='medassist', cursorclass=sql.cursors.DictCursor)
      cmd=db.cursor(sql.cursors.DictCursor)
      return (db,cmd)