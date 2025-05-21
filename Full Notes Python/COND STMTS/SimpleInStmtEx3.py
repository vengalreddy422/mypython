#Program for accepting a Numerical +ve value and decide whether It is Even OR Odd
#SimpleInStmtEx3.py
n=float(input("Enter a Numerical value:"))
if(n<=0):
    print("\t{} Invalid Input".format(n))
if (n>0) and (n%2==0):
    print("\t{} is Even Number:".format(n))
if(n>0) and (n%2!=0):
    print("\t{} is Odd Number:".format(n))