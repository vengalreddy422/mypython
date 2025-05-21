#Program for Demonstrating the Need of  Variable Length Arguments
# This Program will Execute as It is 
#PureVarLengthArgsEx1.py

def   disp( *kvr): # Here *kvr is called Variable Length argument and It holds Var Lengths args and whose type is tuple
	print(kvr,type(kvr))


#Main Program--Family Similar Function Calls with Variable Length args
disp(10,20,30,40,50) # Function Call-1 with 5 Args
disp(10,20,30,40)# Function Call-2 with 4 Args
disp(10,20,30)# Function Call-3 with 3 Args
disp(10,20)# Function Call-4 with 2 Args
disp(10)# Function Call-5 with 1 Arg
disp()# Function Call-6 with 0 Args

