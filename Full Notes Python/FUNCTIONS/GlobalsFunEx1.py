#Program for Demonstrating the Need of globals()
#NOTE: In This Program, we have Different global and local Variable Names.
#GlobalsFunEx1.py
a=10
b=20
c=30
d=40 # Here 'a' , 'b' , 'c' and 'd' are called global Variables
def  operation():
	x=100
	y=200
	z=300
	k=400 # Here x,y,z,k are called Local Variables
	res=a+b+c+d+x+y+z+k
	print("sum=",res)

#Main Program
operation()

