#Program for Inserting Employee Record in employee table by reading Values from KBD
#OracleRecordInsertEx1.py
import oracledb as orc # Step-1
def recordinsert():
    try:
        conobj = orc.connect("system/tiger@localhost/orcl")  # Step-2
        curobj = conobj.cursor()  # Step-3
        # Step-4
        iq="insert into employee values(250,'Mansi',5.3,'TCS')"
        curobj.execute(iq)
        conobj.commit()
        print("{} Record Inserted".format(curobj.rowcount)) # Step-5
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:", db)

#Main Program
recordinsert()