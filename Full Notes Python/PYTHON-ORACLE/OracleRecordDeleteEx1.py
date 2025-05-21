#program for Deleting the Record Based on Employee Number
#OracleRecordDeleteEx1.py
import oracledb as orc
def recorddelete():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        dq="delete from employee where eno=115"
        cur.execute(dq) # OR cur.execute("delete from employee where eno=115")
        con.commit()
        if(cur.rowcount>0):
            print("\t{} Record Deleted".format(cur.rowcount))
        else:
            print("\tRecord does not exist")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#main program
recorddelete()