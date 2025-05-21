import oracledb as orc

class Deleterecord:
    def readvalue(self):
        self.stno=float(input("Enter student Number To delete Record:"))
    def removerecord(self):
        while(True):
            try:
                conobj=orc.connect("system/yash@localhost/orcl")
                curobj=conobj.cursor()
                self.readvalue()
                curobj.execute("select *from student Where stno=%d" %self.stno)
                record=curobj.fetchone()
                if(record==None):
                    print("student Record Does Not Exist")
                else:
                    curobj.execute("delete from student where stno=%d" %self.stno)
                    print("{} Record deleted".format(curobj.rowcount))
                    conobj.commit()
                ch1 = False
                while (True):
                    ch = input("Do you Want to delete Another Record:")
                    if (ch.lower() == "no"):
                        ch1 = True
                        break
                    elif (ch.lower() == "yes"):
                        break
                    else:
                        print("\tPlease Enter either yes or no try-again")
                if (ch1):
                    break
            except ValueError:
                print("\tDon't Enter strs,alnums and symbol for student Number")

