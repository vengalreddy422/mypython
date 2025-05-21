#Program for accepting Two Numerical Values and find Biggest among them
# and check for equality
#TernaryOpEx3.py
a=float(input("Enter Value of a:")) # a=10
b=float(input("Enter Value of b:")) # b=10
#Fin Biggest among them anc check for equality
res= a if a>b else b if b>a else "Both Values are Equal"
print("big({},{})={}".format(a,b,res))
