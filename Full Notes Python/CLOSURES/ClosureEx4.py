#ClosureEx4.py
def counterinformation():  #  Outer Function
	counter=0 # Local Variable in Outer Function
	def  operation(): # Inner Function--Closure
		nonlocal counter
		counter=counter+1
		return counter
	return operation

#Main Program
op=counterinformation()
print("First Time=",op())
print("Second Time=",op())
print("Third Time=",op())
