#Program for deciding whether the Given Number is Prime or Not
#BreakStmtEx5.py
n=int(input("Enter any Number:"))
if(n<=1):
    print("\t{} is Invalid Input".format(n))
else:
    res="Prime"
    for i in range(2,n):
        if(n%i==0):
            res="Not Prime"
            break
    print("{} is {}".format(n,res))

