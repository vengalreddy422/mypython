#Program for Display for EMul Table for  N where N is +ve
#ForLoopEx5.py
n=int(input("Enter a Number for Generating Mul table:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-" * 50)
    print("Mul Table for :{}".format(n))
    print("-" * 50)
    for i in range(1,11):
        print("\t{} x {}={}".format(n,i,n*i))
    else:
        print("-"*50)