import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
print("connected")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE aptechinfo2")