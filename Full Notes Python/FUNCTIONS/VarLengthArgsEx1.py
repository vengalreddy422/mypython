#Program for Demonstrating the Need of  Variable Length Arguments
#NOTE: This Program will not Execute as It is bcoz PVM Remembers Latest Function Def (in the case same fucntion names)  Only and More Over PVM Performs Interpretation Process.
#VarLengthArgsEx1.py
def  disp(a,b,c,d,e): # Function Def-1 with 5 Params
	print(a,b,c,d,e) 
def  disp(a,b,c,d): # Function Def-2 with 4 Params
	print(a,b,c,d)  
def  disp(a,b,c): # Function Def-3 with 3 Params
	print(a,b,c)  
def  disp(a,b): # Function Def-4 with 2 Params
	print(a,b)  
def  disp(a): # Function Def-5 with 1 Param
	print(a)  
def  disp(): # Function Def-6 with 0 Param
	print("empty")  

#Main Program--Family Similar Function Calls with Variable Length args
disp(10,20,30,40,50) # Function Call-1 with 5 Args
disp(10,20,30,40)# Function Call-2 with 4 Args
disp(10,20,30)# Function Call-3 with 3 Args
disp(10,20)# Function Call-4 with 2 Args
disp(10)# Function Call-5 with 1 Arg
disp()# Function Call-6 with 0 Args

