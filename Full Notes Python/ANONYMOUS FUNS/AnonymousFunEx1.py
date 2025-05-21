#Define the function for addition of Two Numbers
#AnonymousFunEx1.py
def addop(a,b):# Normal Function Def.
    return(a+b)

sumop=lambda  k,v: k+v # Anonymous Function Def

#Main Program
print("type of addop=",type(addop))
res=addop(10,20)
print("Sum by using Normal Function=",res)
print("------------------------------------")
print("Type of sumop=",type(sumop)) # <class 'function'>
res1=sumop(20,30)
print("Sum by using Anonymous Function=",res1)
