#Non-ConstEx.py
class Student:
    def getsuddata(self):
        self.sno=100
        self.name="Rossum"
#Main Program
s=Student() # Object Creation
print("content of s=",s.__dict__)
s.getsuddata()
print("content of s=",s.__dict__)
