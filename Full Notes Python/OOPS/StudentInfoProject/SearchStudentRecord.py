import oracledb as orc
class Searchstudent:
    def getstudentNumber(self):
        self.stno=int(input("Enter Student Number to Search:"))

    def serchstudentrecord(self):
        while(True):
            try:
                conobj=orc.connect("system/yash@localhost/orcl")
                curobj=conobj.cursor()
                self.getstudentNumber()
                curobj.execute("select *from student where stno=%d" %self.stno)
                record=curobj.fetchone()
                if(record==None):
                    print("Student Record Does not Exist")
                else:
                    print("\tStudent Record Exist")
            except orc.DatabaseError as db:
                print("Problem in oracle db",db)
            except ValueError:
                print("\tDon't enter strs,alnums and symbols")
            else:
                ch1 = False
                while (True):
                    ch = input("Do you Want to search Another Record:")
                    if (ch.lower() == "no"):
                        ch1 = True
                        break
                    elif (ch.lower() == "yes"):
                        break
                    else:
                        print("\tPlease Enter either yes or no try-again")
                if (ch1):
                    break


