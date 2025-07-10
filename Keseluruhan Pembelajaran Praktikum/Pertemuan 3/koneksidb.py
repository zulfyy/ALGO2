import mysql.connector

mydb = mysql.connector.connect(
    host    = "localhost",
    user    = "root",
    password = "",
    database = "db_python2o"
)

print("Berhasil terkoneksi & masuk!")



