#Function Def for "adding of two numbers"
# INPUTS     :  Taking from function call
# PROCESS    :  Done in Function Body
# RESULT     :  Giving Result to Function call
#ApproachEx1.py
def addop(k,v): # Here 'k' and 'v' are called formal Parameters
    r=k+v # Here 'r' is called local variable
    return r

#main Program
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
c=addop(a,b) # Function Call with Inputs and Gets result from Function Def
print("Sum({},{})={}".format(a,b,c))
print("---------------OR--------------------------")
k=float(input("Enter First Value:"))
v=float(input("Enter Second Value:"))
r=addop(k,v) # Function Call with Inputs and Gets result from Function Def
print("Sum({},{})={}".format(k,v,r))