#Program for Creating a Table Employee in MYSQL
#MySQLTableCreateEx.py
import mysql.connector
def tablecreate():
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="root",
                                    database="batch11am")
        cur=con.cursor()
        #Create table employee
        tc="create table student(sno int primary key,name varchar(10) not null,marks float not null)"
        cur.execute(tc)
        print("Table Created in MySQL--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in MYSQL: ",db)

#Main Program
tablecreate()