#program for Demonstrating the Need of Class Level Method
#ClassLevelMethodNameEx4.py
class Student:
    @classmethod
    def getcrs(cls): # Class Level Method
        cls.crs="PYTHON" # OR Student.crs="PYTHON"
        cls.getcity() # Class Level Method Calling another Class Level Method w.r.t cls
    @classmethod
    def getcity(cls):
        cls.city="HYD"

#Main Program
s=Student()
s.getcrs()# Calling the Class Level Method Name w.r.t Object Name
#display Class Level Data Member Name
print("Student Course:{}".format(Student.crs))
print("Student Course:{}".format(Student.city))