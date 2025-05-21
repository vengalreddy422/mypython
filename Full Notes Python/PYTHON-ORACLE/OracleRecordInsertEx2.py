#Program for Inserting Employee Record in employee table by reading Values from KBD
#OracleRecordInsertEx2.py
import oracledb as orc # Step-1
def recordinsert():
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
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:", db)

#Main Program
recordinsert()