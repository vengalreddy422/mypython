#Program for Creating a Table employee in Oracle
#OracleTableCreateEx.py
import oracledb as orc # Step-1
def tablecreate():
    try:
        conobj=orc.connect("system/tiger@localhost/orcl")#Step-2
        curobj=conobj.cursor() # Step-3
        #Step-4
        tc="create table teacher(tno number(2) primary key,tname varchar2(10) not null,sal number(5,2) not null)"
        curobj.execute(tc)
        print("Table Created Successfully--verify") # Step-5
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main Program
tablecreate() # Function Call