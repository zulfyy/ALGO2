import mysql.connector

mydb = mysql.connector.connect(
    host    = "localhost",
    user    = "root",
    password = ""
)

print("Berhasil connect!")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS db_python2o")
print("Database berhasil dibuat!")

