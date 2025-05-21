#Program for reading the employee records
# from the file where employee records present
#EmpUnPickEx1.py
import pickle
def readrecords():
    with open("emp.pick","rb") as fp:
        print("="*50)
        while(True):
            try:
                record=pickle.load(fp)
                for val in record: # [100, 'RS', 2.3]
                    print("\t{}".format(val),end="\t")
                print()
            except EOFError:
                print("=" * 50)
                break
#Main Program
readrecords()