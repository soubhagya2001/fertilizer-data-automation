import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="",database="test_db")

if connection.is_connected():
    print("Connected successfully")
else:
    print("Failed to connect")