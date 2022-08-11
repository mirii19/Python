import pymysql as sql
conexion = sql.connect(host='localhost',user='root',password='',database='bdcurso')

cursor=conexion.cursor()
cursor.execute("SELECT * FROM 'demo' where 'id' = 5")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()

conexion.close()