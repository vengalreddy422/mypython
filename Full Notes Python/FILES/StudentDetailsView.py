#StudentDetailsView.py
import pickle
def recordview():pass

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


