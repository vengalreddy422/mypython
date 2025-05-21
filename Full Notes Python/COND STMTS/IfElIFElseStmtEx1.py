#Program for Deciding weather the Given Number +Ve or -Ve or Zero
#IfElIFElseStmtEx1.py
n=float(input("Enter a Number:")) # n--- -23
if(n>0):
    print("{} is +VE Value".format(n))
elif(n<0):
    print("{} is -VE Value".format(n))
elif(n==0):
    print("{} is ZERO".format(n))
else: # Optional to write
    print("I am from else part")
print("Program execution Compelted")