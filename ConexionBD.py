#Añadir datos a una base de datos MySQL
import pymysql as sql
conexion = sql.connect(host='localhost',user='root', password='',database='bdcurso')

cursor=conexion.cursor()
cursor.execute("create table demo (id INT, datos VARCHAR (100));")
#Inserción a la tabla BD
cursor.execute("INSERT into demo (id,datos) VALUES ('5','curso')")
#Guardar los cambios que hemos realizado
conexion.commit()
conexion.close()

