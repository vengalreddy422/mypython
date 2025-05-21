#EmployeePick.py
from Employee import Employee
import pickle
class EmpPickEx:
    def saveempdata(self):
        with open("emp.pick","ab") as fp:
            while(True):
                #Accept the employee from KBD
                print("-------------------------------------")
                empno=int(input("Enter Employee Number:"))
                empname=input("Enter Employee Name:")
                empsal=float(input("Enter Employee Salary:"))
                print("-------------------------------------")
                #create an object of Employee Class of Employee Module
                eo=Employee(empno,empname,empsal)
                #Save the employee Object data into the file
                pickle.dump(eo,fp)
                print("Employee Record Saved in File")
                print("-------------------------------------")
                ch=input("Do u want Insert Another Record(yes/no):")
                if(ch.lower()=="no"):
                    print("Thx for using this Program")
                    break

#main Program
epx=EmpPickEx()
epx.saveempdata()