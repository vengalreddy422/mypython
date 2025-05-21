#Program for altering by adding New column Name to the Employee Table
#OracleAlterTablewithAdd.py
import oracledb as orc
def alterwithadd():
    try:
        conobj=orc.connect("system/tiger@localhost/orcl")#Step-2
        curobj=conobj.cursor() # Step-3
        #Step-4
        aq="alter table employee add(compname varchar2(10) not null)"
        curobj.execute(aq)
        print("Table altered Successfully--verify") # Step-5
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main Program
alterwithadd()