#EmployeeUnPick.py
import pickle
class EmployeeUnPick:
    def readempvals(self):
        with open("emp.pick","rb") as fp:
            print("*" * 50)
            while(True):
                try:
                    empobj = pickle.load(fp)
                    empobj.dispempvals()
                except EOFError:
                    print("*"*50)
                    break

#Main Program
eo=EmployeeUnPick()
eo.readempvals()