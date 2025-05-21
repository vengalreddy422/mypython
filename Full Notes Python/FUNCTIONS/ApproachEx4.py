#Function Def for "adding of two numbers"
# INPUTS     : Taking  in Function Body
# PROCESS    : Done in Function Body
# RESULT     : Giving Result to Function call
#ApproachEx4.py
def addop():
    # Take Input
    k = float(input("Enter First Value:"))
    v = float(input("Enter Second Value:"))
    #Do the Process
    r=k+v
    #give Result to function
    return k,v,r

#Main Program
k,v,r=addop() # Function Call with Multi Line assignment
print("sum({},{})={}".format(k,v,r))
print("------------OR----------------------")
res=addop()# Function Call with single Line assignment
# Here res is of type <class, tuple>
print("sum({},{})={}".format(res[0],res[1],res[2]))
print("------------OR---------------------")
print("sum({},{})={}".format(res[-3],res[-2],res[-1]))

