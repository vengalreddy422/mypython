#IterEx8.py
import sys
x="PYTHON"
print("------------------------------------------------------")
print("Content of x =",x)
print("Type of x=",type(x))
print("------------------------------------------------------")
#Convert Iterable Object x into Iterator Object by using iter()
itrobj=iter(x)
print("Type of iterobj=",type(itrobj))
for val in itrobj:
	print(val)