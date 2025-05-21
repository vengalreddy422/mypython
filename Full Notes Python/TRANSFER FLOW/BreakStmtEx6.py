#Program for deciding whether the Given Number is Prime or Not
#BreakStmtEx6.py
n=int(input("Enter any Number:"))
if(n<=1):
    print("\t{} is Invalid Input".format(n))
else:
    res=True
    for i in range(2,n):
        if(n%i==0):
            res=False
            break

    r="Prime" if res else "Not Prime"
    print("{} is {}".format(n,r))

