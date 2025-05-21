#StudentAdd.py<--File Name and Module Name
import pickle,sys
sys.path.append("E:\\KVR-PYTHON-6PM\\EXCEPTION HANDLING\\CASE STUDY-2")
from NameValidationProcess import validate
from NameValidationExcept import SpaceError, ZeroLengthError, InvalidNameError
def duplicate(stno):
    studrecords=[]
    with open("student.pick","rb") as fp:
        while(True):
            try:
                record=pickle.load(fp)
                studrecords.append(record)
            except EOFError:
                break
        dupl=False
        for rec in studrecords:
            if(rec[0]==stno):
                dupl=True
                break
        return dupl

def recordadd():
    with open("student.pick","ab") as fp:
        while(True):
            try:
                print("-"*60)
                stno=int(input("Enter Student Number:"))
                sname=validate(input("Enter Student Name:"))
                marks=float(input("Enter Student Marks:"))
                colname=validate(input("Enter Student College Name:"))
                print("-" * 60)
                stlist=list()
                stlist.append(stno)
                stlist.append(sname)
                stlist.append(marks)
                stlist.append(colname)
                #save stlist data to the file
                if(not duplicate(stno)):
                    pickle.dump(stlist,fp)
                    print("\tStudent Record Inserted")
                else:
                    print("Record already Exist on {} Number".format(stno))
                print("-" * 60)
                ch=input("Do u want to Insert Another Record(yes/no):")
                if(ch.lower()=="no"):
                    break
            except ValueError:
                print("\tDon't enter alnums,strs and symbols for stno and Marks")
            except SpaceError:
                print("\tDon't Enter Space space for Ur Name / Col Name:")
            except ZeroLengthError:
                print("\tU Must Enter UR name/ Col Name:")
            except InvalidNameError:
                print("\tUr Name/ Col Name: is Invalid")

