#Program for Getting Records along with Column Names for Of Table
#MySQLSelectRecordsWithColNamesEx.py
import mysql.connector as orc
def getrecordswithcolnames():
    try:
        con = orc.connect(host="localhost",
                          user="root",
                          passwd="root",
                          database="batch11am")
        cur = con.cursor()
        sq = "select * from employee order by name "
        cur.execute(sq)
        #Code for Getting the Col Names
        print("-"*50)
        colinfo=cur.description # Here type of colinfo is list
        #Here description is an attribute which is used for Getting the Colnames of Table
        for column in colinfo:
            print(column[0],end="\t\t")
        print()
        print("-" * 50)
        #Code for Getting the Records
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val),end="\t\t")
            print()
        print("-" * 50)
    except orc.DatabaseError as db:
        print("Problem with MYSQL DB:", db)

#Main Program
getrecordswithcolnames()