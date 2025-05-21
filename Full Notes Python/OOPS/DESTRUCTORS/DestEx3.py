#DestEx3.py
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
print("No longer Interested to maintain object memory space e1")
time.sleep(4)
del e1 # GC calls Its Destructor Forcefully
time.sleep(4)
e2=Employee(200,"TR") # Object Creation makes the PVM to Call Parameterized Constructor
print("No longer Interested to maintain object memory space e2")
time.sleep(4)
del e2 # GC calls Its Destructor Forcefully
time.sleep(4)
e3=Employee(300,"DR") # Object Creation makes the PVM to Call Parameterized Constructor
print("No longer Interested to maintain object memory space e3")
del e3 # GC calls Its Destructor Forcefully
time.sleep(4)
print("Program Execution Ended")
print("----------------------------------------------------------")
time.sleep(4)
