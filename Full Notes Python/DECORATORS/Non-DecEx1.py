#Non-DecEx1.py
def  getval():  # Function Defined by KVR
	return float(input("Enter a Number:"))

def square():						
	n=getval()
	res=n**2
	print("Square({})={}".format(n,res))

def squareroot():				
	n=getval()
	res=n**0.5
	print("SquareRoot({})={}".format(n,res))

#Main Program
square()
squareroot()