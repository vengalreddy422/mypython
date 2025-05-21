#program for DUpdate the Record Based on Employee Number
#OracleRecordUpdateEx1.py
import oracledb as orc
def recordupdate():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        uq="update employee set sal=12.35,compname='IBM' where eno=115"
        cur.execute(uq)
        con.commit()
        if(cur.rowcount>0):
            print("\t{} Record Updated-verify".format(cur.rowcount))
        else:
            print("\tRecord Does not Exist")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#main program
recordupdate()