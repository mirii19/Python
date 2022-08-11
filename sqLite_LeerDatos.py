import sqlite3

conexion = sqlite3.connect('bdcurso.bd')

for row in conexion.execute("SELECT * FROM 'datos'"):
    print(row)

conexion.close()