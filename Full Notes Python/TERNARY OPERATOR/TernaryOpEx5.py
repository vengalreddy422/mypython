#Program for accepting Three Numerical Values and find Biggest among them
# and check for equality
#TernaryOpEx5.py
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
c=float(input("Enter Value of c:"))
#Find Biggest among them and check for equality
res=a if (b<=a>c) else b if (a<b>=c) else c if (a<=c>b) else "All Values Equal"
print("big({},{},{})={}".format(a,b,c,res))

