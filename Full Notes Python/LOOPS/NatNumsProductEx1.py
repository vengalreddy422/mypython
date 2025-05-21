#Program for Finding the sum of N Natural Numbers
#NatNumsProductEx1.py
n=int(input("Enter How Many Natural Numbers Product u want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-"*40)
    print("Product of {} Numbers".format(n))
    print("-" * 40)
    p=1 # # Multicative  Identity
    for i in range(1,n+1):
        print("\t\t{}".format(i))
        p=p*i
    else:
        print("-" * 40)
        print("Product={}".format(p))
        print("-" * 40)

