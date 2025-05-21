#Program for obtaining the Col Names from Table
#OracleColumnNamesEx.py
import oracledb as orc
def selectcols():
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
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#main program
selectcols()