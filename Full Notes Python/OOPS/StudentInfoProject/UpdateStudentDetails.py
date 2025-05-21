import oracledb as orc
from Exeptions import SpaceError,ZeroLengthError,InvalidNameError,InvalidMarkError
from NameValidation import validate

class Update:
    def getstudentnumber(self):
            self.stno=int(input("Enter Student Number To update Record:"))

    def getvalues(self):
        while(True):
            try:
                self.sname=validate(input("Enter Student Name: "))
            except SpaceError:
                print("\tDon't Enter space for Student Name / Col Name try-again")
            except ZeroLengthError:
                print("\tU Must Enter Student name try-again")
            except InvalidNameError:
                print("\tstudent Name is Invalid try-again")
            else:
                break

        while(True):
            try:
                self.marks=float(input("Enter Student marks:"))
                if (self.marks > 100 or self.marks < 0):
                    raise InvalidMarkError
            except ValueError:
                print("\tDon't Enter strs,alnums and symbol for student marks try-again")
            except InvalidMarkError:
                print("\tPlease enter Valid marks")
            else:
                break
        while(True):
            try:
                self.collegename=validate(input("Enter student college Name:"))
            except SpaceError:
                print("\tDon't Enter space for Student  Col Name try-again")
            except ZeroLengthError:
                print("\tU Must Enter college name try-again")
            except InvalidNameError:
                print("\tcollege Name is Invalid try-again")
            else:
                break

    def updateRecord(self):
        while(True):
            try:
                conobj=orc.connect("system/yash@localhost/orcl")
                curobj=conobj.cursor()
                while(True):
                     try:
                         self.getstudentnumber()
                     except ValueError:
                         print("\tDon't enter strs,alnums and symbol  ")
                     else:
                         break

                curobj.execute("select *from student where stno=%d" %self.stno)
                record=curobj.fetchone()
                if(record==None):
                    print("\tRecord Does Not Exist")
                    print()
                else:
                    self.getvalues()
                    curobj.execute("update student set sname='%s',smarks=%f,collegename='%s' where stno=%d"%(self.sname,self.marks,self.collegename,self.stno))
                    if(curobj.rowcount>0):
                        print("\t{} Record updated ".format(curobj.rowcount))
                    conobj.commit()
            except orc.DatabaseError as db:
                print("Problem in oracle DB:",db)
            else:
                ch1 = False
                while (True):
                    ch = input("Do you Want to Update Another Record:")
                    if (ch.lower() == "no"):
                        ch1 = True
                        break
                    elif (ch.lower() == "yes"):
                        break
                    else:
                        print("\tPlease Enter either yes or no try-again")
                if (ch1):
                    break
