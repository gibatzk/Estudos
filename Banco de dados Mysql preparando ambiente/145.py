import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gilberto",
    password="abc123",
    database="mygilbertotezuka"
)



mycursor = mydb.cursor()

    # sql = """CREATE TABLE pessoas (
    #              id INT AUTO_INCREMENT PRYMARY KEY,
    #              nome VARCHAR(255), 
    #              idade iNT(2)
    #          )"""

sql = "ALTER TABLE pessoas ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST"

mycursor.execute(sql)