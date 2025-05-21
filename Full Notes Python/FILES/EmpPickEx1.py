#Program for Reading employee Values from KBD
# and Save them in File by using Pickling Process
#EmpPickEx1.py
import pickle
def saverecord():
    with open("emp.pick","ab") as fp:
        #Read Employee Values from KBD
        print("-----------------------------------")
        empno=int(input("Enter Employee Number:"))
        empname=input("Enter Employee Name:")
        empsal=float(input("Enter Employee Salary:"))
        print("-----------------------------------")
        #Create a List for placing emp values
        lst=[]
        lst.append(empno)
        lst.append(empname)
        lst.append(empsal)
        #Save lst data into file by using dump()
        pickle.dump(lst,fp)
        print("Employee Record Saved into the File")
        print("-----------------------------------")

#Main Program
saverecord()