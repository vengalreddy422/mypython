#Program for Obtaining the connection from Oracle db
#OracleConnTestEx2.py
import oracledb as orc # Step-1
def getconnection():
    try:
        conobj=orc.connect("system/tiger@127.0.0.1/orcl") # Step-2
        print("Type of conobj=",type(conobj))
        print("Python Program Got Connection from Oracle Database")
    except orc.DatabaseError as db:
        print("Problem with Oracle DB: ",db)

#main Program
getconnection() # Function Call