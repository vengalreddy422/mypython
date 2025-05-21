#Program for Demonstarting the Need of Instance Method
# and How self contains Current Object Address.
#InstanceMethodEx1.py
class Student:
    def readstudvals(self):
        print("I am from readstudvals()")
        print("Current Object Address/Ref=",id(self))
        print("------------------------------------")

#Main Program
so1=Student() # Object Creation
print("ID of so1 in Main Program=",id(so1))
so1.readstudvals()
#-------------------------------------------
so2=Student() # Object Creation
print("ID of so2 in Main Program=",id(so2))
so2.readstudvals()


