#Program for Obtaining the connection from Oracle db
#OracleConnTestEx1.py
import oracledb as orc # Step-1
try:
    conobj=orc.connect("system/tiger@localhost/orcl") # Step-2
    print("Type of conobj=",type(conobj))
    print("Python Program Got Connection from Oracle Database")
except orc.DatabaseError as db:
    print("Problem with Oracle DB: ",db)
