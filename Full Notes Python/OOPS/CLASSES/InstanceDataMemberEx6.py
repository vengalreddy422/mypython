#Program for adding Two Numbers by using Classes and Objects
class Sum:pass

#Main Program
so=Sum() # Object Creation
#read Two values in object so---
so.a=float(input("Enter First Value:"))
so.b=float(input("Enter Second Value:"))
#add the Values of Object so
so.c=so.a+so.b
print("Sum({},{})={}".format(so.a,so.b,so.c))


