#StudentDetailsView.py
import pickle
def recordview():
    studrecords = []
    with open("student.pick", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                studrecords.append(record)
            except EOFError:
                break
        #Accept the Student Number and Display the Details
        sno=int(input("Enter Student Number to View Details:"))
        found=False
        for record in studrecords:
            if(record[0]==sno):
                found=True
                rec=record
                break
        if(found):
            print("--------------------------------------")
            print("\tStudent Number={}".format(record[0]))
            print("\tStudent Name={}".format(record[1]))
            print("\tStudent Marks={}".format(record[2]))
            print("\tStudent College Name={}".format(record[3]))
            print("--------------------------------------")
        else:
            print("Student Record Does Not Exist")


def recordsview():
    with open("student.pick","rb") as fp:
        print("*"*50)
        print("\tSTNO\tNAME\tMARKS\tCOLNAME")
        print("*" * 50)
        while(True):
            try:
                record=pickle.load(fp)
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
            except EOFError:
                print("*" * 50)
                break


