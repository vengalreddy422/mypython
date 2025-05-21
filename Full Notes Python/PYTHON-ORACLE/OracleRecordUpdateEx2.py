#program for DUpdate the Record Based on Employee Number
#OracleRecordUpdateEx2.py
import oracledb as orc
def recordupdate():
    while(True):
        try:
            con=orc.connect("system/tiger@localhost/orcl")
            cur=con.cursor()
            #Accept the empoloyee Number,new sal and New comp name
            empno=int(input("Enter Employee Number for Updating Other Deatils:"))
            newsal=float(input("Enter Employee New Salary:"))
            newcompname = input("Enter Employee New Comp Name:")
            uq="update employee set sal=%f,compname='%s' where eno=%d"
            cur.execute(uq %(newsal,newcompname,empno))
            con.commit()
            if(cur.rowcount>0):
                print("\t{} Record Updated-verify".format(cur.rowcount))
            else:
                print("\tRecord Does not Exist")
            ch = input("Do u want Update Another Record(yes/no):")
            if (ch.lower() == "no"):
                print("Thx for Using This Program")
                break
        except orc.DatabaseError as db:
            print("Problem in Oracle DB:",db)
        except ValueError:
            print("\tDon't Enter alnums,strs and symbols for emp number and Salaryt-try again")

#main program
recordupdate()