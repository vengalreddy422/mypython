#Program for Deciding weather the Given Number +Ve or -Ve or Zero
#IfElseStmtEx2.py
n=float(input("Enter a Number:")) # n--- -23
if(n>0):
    print("{} is +VE Value".format(n))
else:
    if(n<0):
        print("{} is -VE Value".format(n))
    else:
        print("{} is ZERO".format(n))
    print("I am in Inner if--else stmt")
print("I am in outer if--else stmt")