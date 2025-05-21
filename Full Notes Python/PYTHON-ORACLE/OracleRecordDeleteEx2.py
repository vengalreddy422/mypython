#program for Deleting the Record Based on Employee Number
#OracleRecordDeleteEx2.py
import oracledb as orc
def recorddelete():
    while(True):
        try:
            con=orc.connect("system/tiger@localhost/orcl")
            cur=con.cursor()
            #get employee Number from KBD
            empno=int(input("Enter Employee Number for Deleting the Record:"))
            dq="delete from employee where eno=%d" %empno
            cur.execute(dq)
            #OR
            #cur.execute("delete from employee where eno=%d" %empno)
            con.commit()
            if(cur.rowcount>0):
                print("\t{} Record Deleted".format(cur.rowcount))
            else:
                print("\tRecord does not exist")
            ch=input("Do u want delete Another Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for Using This Program")
                break
        except orc.DatabaseError as db:
            print("Problem in Oracle DB:",db)
        except ValueError:
            print("Don't Enter alnums,strs and symbols for emp number-try again")

#main program
recorddelete()