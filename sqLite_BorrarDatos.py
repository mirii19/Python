from multiprocessing import context
import sqlite3
from tkinter import SW

conexion = sqlite3.connect('bdcurso.bd')

query = "DELETE FROM 'datos' where id='1'"

conexion.execute(query)
conexion.commit
conexion.close()