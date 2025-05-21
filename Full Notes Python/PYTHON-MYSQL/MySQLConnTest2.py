#Program for Getting the Connection from MYSQL
#MySQLConnTest2.py
import mysql.connector
con=mysql.connector.connect(host="127.0.0.1",
                    user="root",
                    passwd="root")
print("Python Program Got connection from MYSQL DB")
