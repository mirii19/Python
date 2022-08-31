import pymysql as sql

db = sql.connect(host="localhost", user="root", passwd="", db="Python")

cursor = db.cursor()

cursor.execute("SELECT * FROM tabla1")
