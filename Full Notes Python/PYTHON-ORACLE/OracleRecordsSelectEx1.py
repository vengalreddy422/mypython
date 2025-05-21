#Program for Reading the Records from Employee Table
# by using fetchone()
#OracleRecordsSelectEx1.py
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
        while(True):
            record = cur.fetchone()
            if(record!=None):
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
            else:
                break
        print("*" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#main program
recordsselect()