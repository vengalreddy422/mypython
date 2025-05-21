#DestEx2.py
import sys
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parameterized Constructor--ID=",id(self))
		self.eno=eno
		self.ename=ename
		print("\tEmployee Number:{}".format(self.eno))
		print("\tEmployee Name:{}".format(self.ename))
		print("----------------------------------------------------------")
	def  __del__(self):
		print("GC calls __del__() for De-allocating Memory Space--ID=",id(self))
		global totmemspace
		totmemspace=totmemspace-sys.getsizeof(self)
		print("Now  Available Memory Space=",totmemspace)

#Main Program
print("----------------------------------------------------------")
print("Program Execution Started")
print("----------------------------------------------------------")
e1=Employee(100,"RS") # Object Creation makes the PVM to Call Parameterized Constructor
e2=Employee(200,"TR") # Object Creation makes the PVM to Call Parameterized Constructor
e3=Employee(300,"DR") # Object Creation makes the PVM to Call Parameterized Constructor
totmemspace=sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)
print("Initially Total Memory Space=",totmemspace)
print("Program Execution Ended")
print("----------------------------------------------------------")
#GC calls Destructor by default at the end of the Program automatically / Implictly--Known as Automatic Garbage Collection.
