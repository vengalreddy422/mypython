#Program for accepting student details and save them as record in Student table of Oracle
#InstanceMethodEx10.py
import oracledb as orc
class Student:
    def getStudVals(self):
        self.sno=int(input("\tEnter Student Number:"))
        self.name=input("\tEnter Student Name:")
        self.marks=float(input("\tEnter Student Marks:"))
    def savestuddata(self):
        self.getStudVals()
        #u must Database Connection Code with Oracle
        try:
            con=orc.connect("system/tiger@localhost/orcl")
            cur=con.cursor()
            iq="insert into student values(%d,'%s',%f)"
            cur.execute(iq %(self.sno,self.name,self.marks))
            con.commit()
            print("{} Record Inserted".format(cur.rowcount))
        except orc.DatabaseError as db:
            print("Problem in Oracle in DB:",db)

#Main Program
s=Student()
while(True):
    s.savestuddata()
    ch=input("Do u want to Insert Another Record(yes/no):")
    if(ch.lower()=="no"):
        print("Thx for using program")
        break
