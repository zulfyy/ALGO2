import mysql.connector

mydb = mysql.connector.connect(
    host    = "localhost",
    user    = "root",
    password = "",
    database = "db_python2o"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customer (name varchar(255), address varchar(255))")
print("Tabel berhasil dibuat!")

