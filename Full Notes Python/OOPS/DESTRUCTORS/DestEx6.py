#DestEx5.py
import time
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parameterized Constructor")
		self.eno=eno
		self.ename=ename
		print("\tEmployee Number:{}".format(self.eno))
		print("\tEmployee Name:{}".format(self.ename))
		print("----------------------------------------------------------")
	def  __del__(self):
		print("GC calls __del__() for De-allocating Memory Space")

#Main Program
print("----------------------------------------------------------")
print("Program Execution Started")
print("----------------------------------------------------------")
e1=Employee(100,"RS") # Object Creation makes the PVM to Call Parameterized Constructor
e2=e1 # Deep Copy
e3=e1 # Deep  Copy
print(e1.__dict__,id(e1))
print("No longer Interested to maintain object memory space e1")
time.sleep(4)
del e1 #  GC Will not calls Its Destructor bcoz e2 and e3 points to memory space
print(e2.__dict__,id(e2))
print("No longer Interested to maintain object memory space e2")
time.sleep(4)
del e2 #  GC Will not calls Its Destructor bcoz  e3 points to memory space
print(e3.__dict__,id(e3))
print("No longer Interested to maintain object memory space e3")
time.sleep(4)
del e3 #  GC Will calls Its Destructor bcoz No Objects points to memory space
time.sleep(4)
print("Program Execution Ended")
print("----------------------------------------------------------")

