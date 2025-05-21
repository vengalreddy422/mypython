#Program for Demonstrating Keyword arguments
#KeywordArgsEx1.py
def  disp(a,b,c,d):
	print("\t{}\t{}\t{}\t{}".format(a,b,c,d))

#Main Program
print("-"*40)
print("\tA\tB\tC\tD")
print("-"*40)
disp(10,20,30,40) # Function Call with Pos Args
disp(d=40,b=20,a=10,c=30) # Function Call with Key word args
disp(c=30,d=40,a=10,b=20) # Function Call with Key word args
disp(10,20,d=40,c=30)# Function Call with Pos Args and Key word args
#disp(c=30,d=40,10,20) ----SyntaxError: positional argument follows keyword argument
disp(c=30,d=40,a=10,b=20) # Function Call with Key word args
print("-"*40)
