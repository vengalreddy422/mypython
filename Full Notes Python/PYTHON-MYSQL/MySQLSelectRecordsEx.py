#Program for Reading the Records from Employee Table
#MySQLSelectRecordsEx.py
import mysql.connector as orc
def selectrecord():
    try:
        con = orc.connect(host="localhost",
                              user="root",
                              passwd="root",
                              database="batch11am")
        cur=con.cursor()
        sq="select * from employee"
        cur.execute(sq)
        #get the Records from cursor object by using fetchone()
        print("------------------------------------------------")
        print("\t\tList of Records")
        print("------------------------------------------------")
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("\t{}".format(val),end="\t")
            print()
        print("------------------------------------------------")
    except orc.DatabaseError as db:
        print("Problem with MySQL DB:",db)

#Main Program
selectrecord()