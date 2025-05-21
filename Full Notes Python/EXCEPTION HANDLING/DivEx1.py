#Program for Demonstrating the Need of Exceotion Handling
#Cal Div of Two Numbers
#DivEx1.py
print("Program Execution Started")
s1=input("Enter First value:")
s2=input("Enter Second value:")
#Convert str values into int type
a=float(s1)   #------------------------exception stmt
b=float(s2)   #------------------------exception stmt
print("Val of a:",a)
print("Val of b:",b)
#Cal Div
c=a/b #------------------------exception stmt
print("Div=",c)
print("Program Execution Completed")