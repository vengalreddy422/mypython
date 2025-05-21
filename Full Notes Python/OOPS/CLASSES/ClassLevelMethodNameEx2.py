#program for Demonstrating the Need of Class Level Method
#ClassLevelMethodNameEx2.py
class Student:
    @classmethod
    def getcrs(cls): # Class Level Method
        cls.crs="PYTHON" # OR Student.crs="PYTHON"
        Student.getcity() # Class Level Method Calling another Class Level Method w.r.t Class name
    @classmethod
    def getcity(cls):
        cls.city="HYD"

#Main Program
Student.getcrs()# Calling the Class Level Method Name w.r.t Class Name
#display Class Level Data Member Name
print("Student Course:{}".format(Student.crs))
print("Student Course:{}".format(Student.city))