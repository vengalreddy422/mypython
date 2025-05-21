#Program for Inserting Employee Record in employee table by reading Values from KBD
#OracleRecordInsertEx3.py
import oracledb as orc # Step-1
def recordinsert():
    while(True):
        try:
            conobj = orc.connect("system/tiger@localhost/orcl")  # Step-2
            curobj = conobj.cursor()  # Step-3
            # Step-4
            #Accept the employee Data from Key Board
            print("--------------------------------------")
            empno=int(input("Enter Employee Number:"))
            empname=input("Enter Employee Name:")
            empsal=float(input("Enter Employee Salary:"))
            empcompname=input("Enter Employee Comp Name:")
            print("--------------------------------------")
            iq="insert into employee values(%d,'%s',%f,'%s')"
            curobj.execute(iq %(empno,empname,empsal,empcompname))
            conobj.commit()
            print("{} Record Inserted".format(curobj.rowcount)) # Step-5
            print("--------------------------------------")
            ch=input("Do u want to Insert Another Employee Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using this program")
                break
        except orc.DatabaseError as db:
            print("Problem in Oracle DB:", db)
        except ValueError:
            print("Don't enter alnums,strs and salary for empno,salary-try again ")

#Main Program
recordinsert()