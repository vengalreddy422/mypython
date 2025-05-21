#program for Demonstrating the Need of Class Level Method
#ClassLevelMethodNameEx1.py
class Student:
    @classmethod
    def getcrs(cls): # Class Level Method
        cls.crs="PYTHON" # OR Student.crs="PYTHON"

#Main Program
Student.getcrs()# Calling the Class Level Method Name w.r.t Class Name
#display Class Level Data Member Name
print("Student Course:{}".format(Student.crs))