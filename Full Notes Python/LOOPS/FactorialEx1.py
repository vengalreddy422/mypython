#program for Cal Factorial of a Number
#n!= 1x2x3x.....n
#FactorialEx1.py
n=int(input("Enter a Number for Calculating Factorial:"))
if(n<0):
    print("{} is Invalid Input, can't Cal Factorial".format(n))
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    else:
        print("Factorial({})={}".format(n,fact))
