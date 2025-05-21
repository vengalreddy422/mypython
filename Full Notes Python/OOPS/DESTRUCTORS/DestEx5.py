#DestEx5.py
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
print(e2.__dict__,id(e2))
print(e3.__dict__,id(e3))
print("Program Execution Ended")
print("----------------------------------------------------------")

