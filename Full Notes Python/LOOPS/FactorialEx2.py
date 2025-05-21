#program for Cal Factorial of a Number
#n!= n x n-1 x.......1
#FactorialEx1.py
n=int(input("Enter a Number for Calculating Factorial:"))
if(n<0):
    print("{} is Invalid Input, can't Cal Factorial".format(n))
else:
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    else:
        print("\t{}!={}".format(n,fact))
