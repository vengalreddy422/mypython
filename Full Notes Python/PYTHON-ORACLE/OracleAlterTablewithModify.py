#Program for altering the column sizes of Employee Table
#OracleAlterTablewithModify.py
import oracledb as orc
def alterwithmodify():
    try:
        conobj=orc.connect("system/tiger@localhost/orcl")#Step-2
        curobj=conobj.cursor() # Step-3
        #Step-4
        aq="alter table employee modify(eno number(3),name varchar2(15))"
        curobj.execute(aq)
        print("Table altered Successfully--verify") # Step-5
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main Program
alterwithmodify()