#Python Program obtains the connection from MySQL
#MySQLConnTestEx1.py
import mysql.connector
try:
	print("Hello")
	con=mysql.connector.connect(host="127.0.0.1",user="root",passwd="root")
	print("Python Program Got connection from MySQL")
except mysql.connector.DatabaseError as db:
    print("Problem with MySQL:",db)

	
