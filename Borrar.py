from curses import curs_set
import pymysql as sql
conexion = sql.connect(host='localhost',user='root', password='',database='bdcurso')

cursor=conexion.cursor()
cursor.execute("DELETE FROM 'demo' where 'id' = 5")

conexion.commit()
cursor.close()
conexion.close()