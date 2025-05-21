#Function Def for "adding of two numbers"
#Approach1.py
def addop(a,b): #here 'a' and 'b' are called Formal params
    c=a+b # here 'c' is called Local Variable
    return c

#main Program
res=addop(10,20) # Function Call--here 10 and 20 called Inputs
print("sum=",res)
res1=addop(100,200) # Function Call--here 100 and 200 called Inputs
print("sum=",res1)