#Program for Creating an object of Cursor
#OracleCursorobjEx.py
import oracledb as kvr # Step-1
def createcurobj():
    try:
        conobj=kvr.connect("system/tiger@localhost/orcl") # Step-2
        print("Type of conobj=",type(conobj))
        print("Python Program got connection from Oracle DB")
        print("---------------------------------------------")
        curobj=conobj.cursor()
        print("type of curobj=",type(curobj))
        print("Python Program Created an object of cursor")
        print("---------------------------------------------")
    except kvr.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#main program
createcurobj() # Function call