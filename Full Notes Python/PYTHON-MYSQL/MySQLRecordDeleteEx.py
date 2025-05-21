#Program for Deleting the Record from Employee Table based on Emp Number
#MySQLRecordDeleteEx.py
import mysql.connector as orc
def deleterecord():
    while(True):
        try:
            con = orc.connect(host="localhost",
                                user="root",
                                passwd="root",
                                database="batch11am")
            cur=con.cursor()
            print("-----------------------------------------------")
            empno=int(input("Enter Employee Number to delete a Record:"))
            cur.execute("delete from employee where eno=%d" %empno)
            con.commit()
            if(cur.rowcount>0):
                print("{} Record Deleted".format(cur.rowcount))
            else:
                print("Record does not Exist")
            print("-----------------------------------------------")
            ch = input("Do u want to Delete Another Record(yes/no):")
            if (ch.lower() == "no"):
                print("Thx for Using This Program")
                break
        except orc.DatabaseError as db:
            print("Problem with MySQL DB:",db)
        except ValueError:
            print("Don't enter alnums, strs and symbols-try again")

#Main Program
deleterecord() # Function Call