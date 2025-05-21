#Program for Droping the Data from MySQL
#MySQLDropDatabaseEx.py
import mysql.connector
def dropdb():
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="root")
        cur=con.cursor()
        #drop a Database from MYSQL"
        cur.execute("drop database batch4pm")
        print("database droped from mysql--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in MYSQL: ",db)

#Main Program
dropdb()