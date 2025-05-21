#Program for Demonstrating the need of global keyword
#GlobalKwdEx1.py
def modify1():
	global a
	a=a+1
	
def modify2():
	global a
	a=a*2

#Main Program
a=10 # Here 'a' is called Global Variable
print("Main Program: Before modify1(): Val of a={}".format(a))
modify1() # Function Call
print("Main Program: after modify1(): Val of a={}".format(a))
modify2()
print("Main Program: after modify2(): Val of a={}".format(a))