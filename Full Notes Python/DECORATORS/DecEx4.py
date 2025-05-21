#DecEx4.py
def cube(nit):
	def cubecal():
		n,sqrval,sqrtval=nit()
		cbval=n**3
		return (n,sqrval,sqrtval,cbval)
	return cubecal

def squareroot(hyd):
	def cal():
		n,sqv=hyd()
		sqrtv=n**0.5
		return(n,sqv,sqrtv)
	return cal

def square(kvr): # Decorator Defintion
	def operation(): # Inner Function
		n=kvr()
		return(n,n**2)
	return operation

@cube
@squareroot
@square
def  getval():  # Function Defined by KVR
	return float(input("Enter a Number:"))

#Main Program
n,sqval,sqrtval,cbval=getval() # Normal Function Call
print("Square({})={}".format(n,sqval))
print("SquareRoot({})={}".format(n,sqrtval))
print("Cube({})={}".format(n,cbval))