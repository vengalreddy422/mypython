import oracledb as orc
class View:
    def veiwrecords(self):
        conobj=orc.connect("system/yash@localhost/orcl")
        curobj=conobj.cursor()
        curobj.execute("select *from student")
        print("="*60)
        for colinfo in curobj.description:
            print("\t{}".format(colinfo[0]),end="\t")
        print()
        print("="*60)
        records=curobj.fetchall()
        for record in records:
            for val in record:
                print("\t{}\t".format(format(val)),end="\t")
            print()
        print("="*60)

    def veiwrecord(self):

        while(True):
            try:
                conobj=orc.connect("system/yash@localhost/orcl")
                curobj=conobj.cursor()
                stno=int(input("Enter student Number to View records:"))
                curobj.execute("select *from student where stno=%d" %stno)
                record=curobj.fetchone()
                print("=" * 60)
                for colinfo in curobj.description:
                    print("\t{}".format(colinfo[0]), end="\t")
                print()
                print("=" * 60)
                if(record==None):
                    print("\t\t\tRecord Does Not Exist")
                else:
                    for val in record:
                      print("\t{}\t".format(val),end="\t")
                    print()
                print("="*60)
                ch1 = False
                while (True):
                    ch = input("Do you Want to see Another Student Details:")
                    if (ch.lower() == "no"):
                        ch1 = True
                        break
                    elif (ch.lower() == "yes"):
                        break
                    else:
                        print("\tPlease Enter either yes or no try-again")
                if (ch1):
                    break
            except orc.DatabaseError as db:
                print("problem with oracle DB",db)
            except ValueError:
                print("\tDon't enter strs,alnums and symbols for student Number")




