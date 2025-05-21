#Program for Listing the Primes withing the Range
#ListPrimesEx1.py
n=int(input("Enter the range in which u want Prime Numbers:"))
if(n<=1):
    print("\t{} is Invalid Input".format(n))
else:
    print("List of Primes within :{}".format(n))
    for num in range(2,n+1): # Outer loop-Supply the Number
       res=True
       for i in range(2,num):#Inner Loop-Decides whether Supplied number prime or not
           if(num%i==0):
               res=False
               break
       if(res):
           print("\t{}".format(num))

