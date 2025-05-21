#Program for accepting Two Numerical Values and find Biggest among them
#TernaryOpEx2.py
a=float(input("Enter Value of a:")) # a=10
b=float(input("Enter Value of b:")) # b=30
#Fin Biggest among them
bv =  a  if  a>b  else  b
print("Big({},{})={}".format(a,b,bv))