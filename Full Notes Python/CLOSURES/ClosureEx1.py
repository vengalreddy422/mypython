#ClosureEx1.py
def  outerfunc(x): # Outer Function
	print("I am From Outer Function")
	def innerfunc(y): # inner Function--Called Closure
		print("I am from Inner Function")
		z=x+y
		return z
	return innerfunc

#Main Program
ifc=outerfunc(10) # Outer Function Call
print("Outer Function Call Completed Its Execution")
print("-------------------------------------------------")
res=ifc(5) # Inner Function Call
print("First time=",res)
print("-------------------------------------------------")
res=ifc(15) # Inner Function Call
print("Second time=",res)
