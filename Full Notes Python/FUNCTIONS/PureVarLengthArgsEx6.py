#Program for Demonstrating the Need of  Variable Length Arguments
# This Program will Execute as It is 
#PureVarLengthArgsEx6.py

def   disp(sno,sname,*kvr,city="HYD"): # Here *kvr is called Variable Length argument and It holds Var Lengths args and whose type is tuple
	print("-"*50)
	print("Student Number:{}".format(sno))
	print("Student Name:{}".format(sname))
	print("Student City:{}".format(city))
	s=0
	for val in kvr:
		print("{}".format(val),end=" ")
		s=s+val
	print("sum={}".format(s))
	print("\nNumber of Variable Length Values=",len(kvr))
	print("-"*50)

#Main Program--Family Similar Function Calls with Variable Length args
disp(100,"RS",10,20,30,40,50) # Function Call-1 with 5 Args
disp(200,"TR",10,20,30,40)# Function Call-2 with 4 Args
disp(300,"DR",10,20,30)# Function Call-3 with 3 Args
disp(400,"PT",10,20,city="RSA")# Function Call-4 with 2 Args
disp(500,"JH",10)# Function Call-5 with 1 Arg
disp(600,"DW")# Function Call-6 with 0 Args
#disp(700,"DT",city="USA",1.2,2.3,3.4)# Function Call-6 with 0 Args--SyntaxError: positional argument follows keyword argument
disp(700,"DT",1.2,2.3,3.4,city="USA")


