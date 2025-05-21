#Program for obtaining the Records with Col Names from Table
#OracleRecordsWithColumnNamesEx.py
import oracledb as orc
def selectrecordswithcols():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        #Read OR Select the Records from employee Table
        sq="select * from employee"
        cur.execute(sq)
        #Get the Col Names from cursor object
        print("*"*50)
        for colinfo in cur.description:
            print("\t{}".format(colinfo[0]),end="\t")
        print()
        print("*"*50)
        #get the Records from cursor object
        records=cur.fetchall()
        if(len(records)==0):
            print("\tTable Does Not Contains Records")
        else:
            for record in records:
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
        print("*" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#main program
selectrecordswithcols()