import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gilberto",
    password="abc123",
    database="mygilbertotezuka"
)


mycursor = mydb.cursor()

# sql = '''
#     ALTER TABLE pessoas  ADD sobrenome VARCHAR(255)
# '''
# sql = 'ALTER TABLE pessoas DROP sobrenome'
# sql = 'ALTER TABLE pessoas  ADD sobrenome VARCHAR(255) FIRST'
sql = 'ALTER TABLE pessoas  ADD sobrenome VARCHAR(255) AFTER nome'



mycursor.execute(sql)