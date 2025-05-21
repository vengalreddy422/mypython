#Program for Demonstrating the Need of globals()
#GlobalsFunEx3.py
a=10
b=20 # Here 'a' , 'b' are called global Variables
def  operation():
	dictobj=globals() # It Obtains Visible and Invisible global Variables along with Its Values
	print("-"*50)
	print("Invisible and Visible Global Variables")
	print("-"*50)
	for gvn,gvv in dictobj.items():
		print("\t{}-->{}".format(gvn,gvv))
	print("-"*50)
	print("Programmer-Defined Global Variables-Way-1")
	print("-"*50)
	print("\tVal of Global Var a=",dictobj['a'])
	print("\tVal of Global Var b=",dictobj['b'])
	print("-"*50)
	print("Programmer-Defined Global Variables-Way-2")
	print("-"*50)
	print("\tVal of Global Var a=",dictobj.get('a'))
	print("\tVal of Global Var b=",dictobj.get('b'))
	print("-"*50)
	print("Programmer-Defined Global Variables-Way-3")
	print("-"*50)
	print("\tVal of Global Var a=",globals().get('a'))
	print("\tVal of Global Var b=",globals().get('b'))
	print("-"*50)
	print("Programmer-Defined Global Variables-Way-4")
	print("-"*50)
	print("\tVal of Global Var a=",globals()['a'])
	print("\tVal of Global Var b=",globals()['b'])
	print("-"*50)
	

#Main Program
operation()



