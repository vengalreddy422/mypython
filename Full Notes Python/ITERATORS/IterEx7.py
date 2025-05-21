#IterEx7.py
import sys
x={10:"Python",20:"Java",30:"Django"}
print("------------------------------------------------------")
print("Content of x =",x)
print("Type of x=",type(x))
print("------------------------------------------------------")
#Convert Iterable Object x into Iterator Object by using iter()
itrobj=iter(x)
print("Type of iterobj=",type(itrobj))
for val in itrobj:
	print("{}--->{}".format(val,x.get(val))) # OR print("{}--->{}".format(val,x[val]))