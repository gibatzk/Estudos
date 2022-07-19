import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gilberto",
    password="abc123"
)

print(mydb)