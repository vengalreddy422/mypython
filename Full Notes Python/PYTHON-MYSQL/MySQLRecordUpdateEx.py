#Program for Updating the empsal, comp name based on employee number
#MySQLRecordUpdateEx.py
import mysql.connector as nit
def recordupdate():
    while(True):
        try:
            con = nit.connect(host="localhost",
                              user="root",
                              passwd="root",
                              database="batch11am")
            cur = con.cursor()
            #Get the employee Number, New Sal and New Comp Name
            print("--------------------------------------------")
            empno=int(input("Enter Employee Number:"))
            newsal=float(input("Enter Employee New Salary for Updating:"))
            newcompname=input("Enter Employee New Comp Name:")
            print("--------------------------------------------")
            uq="update employee set sal= %f, compname='%s' where eno=%d"
            cur.execute(uq %(newsal,newcompname,empno))
            con.commit()
            if(cur.rowcount>0):
                print("{} Record Updated--verify".format(cur.rowcount))
            else:
                print("Employee Record does not Exist")
            print("--------------------------------------------")
            ch = input("Do u want to Update Another Record(yes/no):")
            if (ch.lower() == "no"):
                print("Thx for Using This Program")
                break
        except nit.DatabaseError as db:
            print("Problem in MySQL database:",db)
        except ValueError:
            print("Don't enter alnums, strs and symbols-try again")
#Main Program
recordupdate()