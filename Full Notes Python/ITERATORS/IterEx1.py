#IterEx1.py
import sys
x=[10,"Rossum","Python",34.56,True]
print("------------------------------------------------------")
print("Content of x =",x)
print("Type of x=",type(x))
print("------------------------------------------------------")
#Convert Iterable Object x into Iterator Object by using iter()
itrobj=iter(x)
print("Type of iterobj=",type(itrobj))
try:
	print(next(itrobj))
	print(next(itrobj))
	print(next(itrobj))
	print(next(itrobj))
	print(next(itrobj))
	print(next(itrobj))
except StopIteration:
	sys.exit()