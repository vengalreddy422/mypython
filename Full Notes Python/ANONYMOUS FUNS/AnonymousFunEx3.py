#Program for Accepting Two Numerical Values and Find Biggest among them
# and check for Equality
#AnonymousFunEx3.py
findbig=lambda a,b: a if a>b else b if b>a else "Both Values are Equal"
findsmall=lambda a,b: a if a<b else b if b<a else "Both Values are Equal"

#Main Program
print("Enter Two Numerical Values:")
a,b=float(input()),float(input())
maxv=findbig(a,b)
minv=findsmall(a,b)
print("Max({},{})={}".format(a,b,maxv))
print("Min({},{})={}".format(a,b,minv))
