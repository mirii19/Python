import sqlite3

conexion = sqlite3.connect('bdcurso.db')
query = "insert into 'datos' ('id', 'datos') values ('1','30')"

conexion.execute(query)
conexion.commit()
conexion.close()