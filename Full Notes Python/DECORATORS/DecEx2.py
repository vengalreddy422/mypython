#DecEx2.py
def square(kvr): # Decorator Definition
	def operations(): # Inner Function 
		n=kvr()
		res=n**2
		return n,res
	return operations

def  getval():  # Function Defined by KVR
	return float(input("Enter a Number:"))

#Main Program
n,r=square(getval)() # Decorator Call cum Inner Function
print("square({})={}".format(n,r))