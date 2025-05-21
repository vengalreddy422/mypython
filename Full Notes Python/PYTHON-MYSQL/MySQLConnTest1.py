#Program for Getting the Connection from MYSQL
#MySQLConnTest1.py
import mysql.connector
con=mysql.connector.connect(host="localhost",
                    user="root",
                    passwd="root")
print("Python Program Got connection from MYSQL DB")
