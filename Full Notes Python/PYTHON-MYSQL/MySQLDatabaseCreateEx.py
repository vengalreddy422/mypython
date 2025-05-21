#Program for Creating the Database on the name of "batch11am"
#MySQLDatabaseCreateEx.py
import mysql.connector
def createdb():
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="root")
        cur=con.cursor()
        #create a Database on the name of "batch11am"
        dc="create database KVR"
        cur.execute(dc)
        print("database created in mysql--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in MYSQL: ",db)

#Main Program
createdb()