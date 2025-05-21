#program for Demonstrating the Need of Class Level Method
#ClassLevelMethodNameEx5.py
class Student:
    @classmethod
    def getcrs(cls): # Class Level Method
        cls.crs="PYTHON" # OR Student.crs="PYTHON"
        cls.getcity() # Class Level Method Calling another Class Level Method w.r.t cls
    @classmethod
    def getcity(cls):
        cls.city="HYD"

    def dispstuddata(self):
        Student.getcrs() # Instance Method Calling Class Level Method w.r.t Class name
        print("Student Course:{}".format(Student.crs))
        print("Student Course:{}".format(Student.city))


#Main Program
s=Student()
s.dispstuddata() # Calling Instance method w.r.t Object Name
