#Program for Finding the sum of N Natural Numbers
#NatNumsSumEx1.py
n=int(input("Enter How Many Natural Numbers sum u want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-" * 50)
    print("Sum of {} Numbers".format(n))
    print("-" * 50)
    s=0 # Additive Identity--Initlization for accumutaing sum of n numbers
    for i in range(1,n+1):
        print("\t{}".format(i))
        s=s+i # OR s+=i
    else:
        print("-"*50)
        print("Sum={}".format(s))
        print("-" * 50)
