#Program for Demonstrating the Need of Static Method
#StaticMethodEx4.py
class Student:
    def getstuddata(self):
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Enter Student Name:")
        print("---------------------------------")
class Employee:
    def getempdata(self):
        self.eno = int(input("Enter Employee Number:"))
        self.ename = input("Enter Employee Name:")
        self.sal = float(input("Enter Employee Salary:"))
        print("---------------------------------")
class Teacher:
    def getteacherdata(self):
        self.tno = int(input("Enter teacher Number:"))
        self.tname = input("Enter Teacher Name:")
        self.sub = input("Enter Teacher Subject:")
        print("---------------------------------")
class HYD:
    @classmethod
    def acceptobjectdata(cls,objdata,objinfo):
        cls.dispobjectdata(objdata,objinfo) # Caling Static Method w.r.t cls
    @staticmethod
    def  dispobjectdata(objdata,objinfo):
        print("---------------------------------------")
        print("{} Object Information".format(objinfo))
        print("---------------------------------------")
        for dmn,dmv in objdata.__dict__.items():
            print("\t{}---->{}".format(dmn,dmv))
        print("---------------------------------------")

#main Program
so=Student()
eo=Employee()
to=Teacher()
so.getstuddata()
eo.getempdata()
to.getteacherdata()
#-----------------------
HYD.acceptobjectdata(so,"Student") # Calling Class Level Method w.r.t Class Name
HYD.acceptobjectdata(eo,"Employee") # Calling Class Level Method w.r.t Class Name
HYD.acceptobjectdata(to,"Teacher") # Calling Class Level Method w.r.t Class Name
