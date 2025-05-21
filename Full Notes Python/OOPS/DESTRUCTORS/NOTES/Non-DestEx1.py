#Non-DestEx1.py
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parameterized Constructor")
		self.eno=eno
		self.ename=ename
		print("\tEmployee Number:{}".format(self.eno))
		print("\tEmployee Name:{}".format(self.ename))
		print("----------------------------------------------------------")

#Main Program
print("----------------------------------------------------------")
print("Program Execution Started")
print("----------------------------------------------------------")
e1=Employee(100,"RS") # Object Creation makes the PVM to Call Parameterized Constructor
e2=Employee(200,"TR") # Object Creation makes the PVM to Call Parameterized Constructor
print("Program Execution Ended")
print("----------------------------------------------------------")