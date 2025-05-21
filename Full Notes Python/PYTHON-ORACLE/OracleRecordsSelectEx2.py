#Program for Reading the Records from Employee Table
# by using fetchmany(no. of records)
#OracleRecordsSelectEx2.py
import oracledb as orc
def recordsselect():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        #Read OR Select the Records from employee Table
        sq="select * from employee"
        cur.execute(sq)
        #Here cur object contains all reords from employee Table
        print("*"*50)
        records=cur.fetchmany(5)
        for record in records:
            for val in record:
                print("\t{}".format(val),end="\t")
            print()
        print("*" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#main program
recordsselect()