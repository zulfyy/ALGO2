import mysql.connector

mydb = mysql.connector.connect(
    host    = "localhost",
    user    = "root",
    password = "",
    database = "db_python2o"
)

mycursor = mydb.cursor()
sql = "INSERT INTO customer (name,address) VALUES (%s, %s)"
val = ("John", "Banjarmasin")

mycursor.execute(sql, val)
mydb.commit() 

print(mycursor.rowcount, "record inserted.")