#Program for Display for Even Numbers within N where N is +ve
#ForLoopEx4.py
n=int(input("Enter How Many Even Numbers u want to Generate:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("Even Numbers within:{}".format(n))
    if(n%2!=0):
        n=n-1
    for i in range(n,0,-2):
        print("\t{}".format(i))
    print("-------------------------------------")