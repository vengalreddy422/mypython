#DecEx3.py
def square(kvr): # Decorator Defintion
	def operation(): # Inner Function
		n=kvr()
		return(n,n**2)
	return operation

@square
def  getval():  # Function Defined by KVR
	return float(input("Enter a Number:"))

#Main Program
n,res=getval() # Normal Function Call
print("Square({})={}".format(n,res))