#Program for Demonstrating the Need of  Variable Length Arguments
#NOTE: This Program will  Execute as It is.
#VarLengthArgsEx2.py
def  disp(a,b,c,d,e): # Function Def-1 with 5 Params
	print(a,b,c,d,e) 

disp(10,20,30,40,50) # Function Call-1 with 5 Args
#-------------------------------------------------------------------------------------------
def  disp(a,b,c,d): # Function Def-2 with 4 Params
	print(a,b,c,d)  

disp(10,20,30,40)# Function Call-2 with 4 Args
#-------------------------------------------------------------------------------------------
def  disp(a,b,c): # Function Def-3 with 3 Params
	print(a,b,c)  
disp(10,20,30)# Function Call-3 with 3 Args
#-------------------------------------------------------------------------------------------
def  disp(a,b): # Function Def-4 with 2 Params
	print(a,b)  
disp(10,20)# Function Call-4 with 2 Args
#-------------------------------------------------------------------------------------------
def  disp(a): # Function Def-5 with 1 Param
	print(a)  

disp(10)# Function Call-5 with 1 Arg
#-------------------------------------------------------------------------------------------
def  disp(): # Function Def-6 with 0 Param
	print("empty")  
disp()  # Function Call-5 with 0 Arg
#-------------------------------------------------------------------------------------------

#NOTE: Here we have N-Function Calls and having corresponding N-Function Definitions and It is one of the complex Process to Define.
# we Have  N-Function Calls and with concept of Variable length Args, we Define single function definition.