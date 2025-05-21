#Program for Demonstrating the Need of globals()
#NOTE: In This Program, we have Same global and local Variable Names.
#GlobalsFunEx2.py
a=10
b=20
c=30
d=40 # Here 'a' , 'b' , 'c' and 'd' are called global Variables
def  operation():
	a=100
	b=200
	c=300
	d=400 # Here 'a' , 'b' , 'c' and 'd'  are called Local Variables
	res=a+b+c+d+globals()['a']+globals()['b']+globals().get('c')+globals().get('d')
	print("sum=",res)

#Main Program
operation()



