import  oracledb as orc
from Exeptions import InvalidStudentNumber,SpaceError,ZeroLengthError,InvalidNameError,InvalidMarkError,RecordExistError
from NameValidation import validate


class Insertstudent:
        def readvalues(self):

            while(True):
                try:
                    self.stno = int(input("Enter Student Number:"))
                    if( self.stno<100 or self.stno>1000):
                        raise InvalidStudentNumber
                    self.curobj.execute("select *from student where stno=%d" % self.stno)
                    record = self.curobj.fetchone()
                    if (record != None):
                        raise RecordExistError

                except ValueError:
                    print("\tDont Enter Strs,alnums and symbol for student Number try-again")
                except InvalidStudentNumber :
                    print("\tStudent Number must be 100 to 999 try-again")
                except RecordExistError:
                    print("\tStudent Number already exist")
                else:
                    break

            while(True):
                try:
                    self.sname = validate(input("Enter Student Name:"))
                except SpaceError:
                    print("\tDon't Enter space for Student Name / Col Name try-again")
                except ZeroLengthError:
                    print("\tU Must Enter Student name try-again")
                except InvalidNameError:
                    print("\tStudent  Name is Invalid try-again")
                else:
                    break
            while(True):
                try:
                    self.marks = float(input("Enter Student Marks:"))
                    if(self.marks>100 or self.marks<0):
                        raise InvalidMarkError
                except ValueError:
                    print("\tDon't Enter strs,alnums and symbol for marks try-again")
                except InvalidMarkError:
                    print("\tPlease enter Valid marks")
                else:
                    break

            while(True):
                try:
                    self.collegename=validate(input("Enter Student College name:"))

                except SpaceError:
                    print("\tDon't Enter space for Student Name / Col Name try-again")
                except ZeroLengthError:
                    print("\tU Must Enter college name try-again")
                except InvalidNameError:
                    print("\tcollege Name is Invalid try-again")
                else:
                    break

        def savestuddata(self):
            while(True):
                try:
                    self.conobj =orc.connect("system/yash@localhost/orcl")
                    self.curobj =self.conobj.cursor()

                    self.readvalues()
                    iq = "insert into student values(%d,'%s',%f,'%s')"
                    self.curobj.execute(iq % (self.stno,self.sname,self.marks,self.collegename))
                    self.conobj.commit()
                    print("\t{} Record Inserted".format(self.curobj.rowcount))
                except orc.DatabaseError as db:
                    print("Problem in Oracle in DB:", db)

                else:
                    ch1=False
                    while(True):
                        ch=input("Do you Want to insert Another Record:")
                        if(ch.lower()=="no"):
                            ch1=True
                            break
                        elif(ch.lower()=="yes"):
                            break
                        else:
                            print("\tPlease Enter either yes or no try-again")
                    if(ch1):
                        break

