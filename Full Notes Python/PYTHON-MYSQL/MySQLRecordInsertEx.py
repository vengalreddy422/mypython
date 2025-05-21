#Program for reading the Values from KBD and Insert then as Record in Employee Table
#MySQLRecordInsertEx.py
import mysql.connector
#Programmere-Defined Exceptions
class InvalidNameError(Exception):pass
class SpaceError(Exception):pass
class ZeroLengthNameError(Exception):pass
# Hitting the Programmere-Defined Exceptions
def validate(name:str): #name=123Guido Van Rossum
    if(len(name)==0):
        raise ZeroLengthNameError
    elif(name.isspace()):
        raise SpaceError
    else:
        words=name.split() # words=['123Guido','Van','Rossum']
        res=True
        for word in words:
            if(not word.isalpha()):
                res=False
                break
        if(res):
            return name
        else:
            raise InvalidNameError
#We are Defining Our Function for  Handling the Exceptions.
def recordinsert():
    while(True):
        try:
            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="root",
                                          database="batch11am")
            cur = con.cursor()
            #read emp values from KBD
            print("--------------------------------------")
            eno=int(input("Enter Employee Number:"))
            ename=validate(input("Enter Employee Name:"))
            empsal = float(input("Enter Employee Salary:"))
            compname = validate(input("Enter Employee Comp Name:"))
            print("--------------------------------------")
            #iq = "insert into employee values(%d,'%s',%f,'%s')"
            #cur.execute(iq %(eno,ename,empsal,compname))
            #OR
            cur.execute("insert into employee values(%d,'%s',%f,'%s')" %(eno,ename,empsal,compname) )
            con.commit()
            print("{} Record Inserted in Table--verify".format(cur.rowcount))
            print("--------------------------------------")
            ch=input("Do u want to Insert Another Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for Using This Program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySql database:",db)
        except ValueError:
            print("Don't alnums, strs and symbols for empno and salary")
        except InvalidNameError:
            print("\tInvalid Emp Name / Comp Name--try again")
        except SpaceError:
            print("\tDon't Give Space for Emp Name / Comp Name--try again")
        except ZeroLengthNameError:
            print("\tU Must Enter Ur Name / Comp Name-try again")
#Main Program
recordinsert()

