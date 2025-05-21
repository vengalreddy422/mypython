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
        self.getcrs() # Instance Method Calling Class Level Method w.r.t self
        print("Student Course:{}".format(self.crs))
        print("Student Course:{}".format(self.city))


#Main Program
s=Student()
s.dispstuddata() # Calling Instance method w.r.t Object Name
