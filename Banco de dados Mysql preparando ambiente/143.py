import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gilberto",
    password="abc123",
    database="mygilbertotezuka"
)
    

mycursor = mydb.cursor()

# sql = """CREATE TABLE pessoas (
#             nome VARCHAR(255), 
#             idade iNT(2)
#         )"""

# mycursor.execute(sql)

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)


