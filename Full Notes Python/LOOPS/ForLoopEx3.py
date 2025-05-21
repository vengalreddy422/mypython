#Program for Display for Odd Numbers within N where N is +ve
#ForLoopEx3.py
n=int(input("Enter How Many Odd Numbers u want to Generate:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("Odd Numbers within:{}".format(n))
    if(n%2==0):
        n=n-1
    for i in range(n,0,-2):
        print("\t{}".format(i))
    print("----------------------------------")

