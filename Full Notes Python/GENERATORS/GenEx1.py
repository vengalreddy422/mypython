#Program for Demonstrating generator
#GenEx1.py
import sys
def  kvrrange(n):
	i=0
	while(i<=n):
		yield i
		i=i+1

#Main Program
x=kvrrange(6)
print("type of kvrrange=",type(kvrrange)) # <class, 'function'>
print("Type of x=",type(x)) # <class,'generator'>
print("------------------------------------------------------------------------")
#To get the Values from generator--we must make request by using a Function called next(generatorobj)
try:
	print(next(x))
	print(next(x))
	print(next(x))
	print(next(x))
	print(next(x))
	print(next(x))
	print(next(x))
	print(next(x))
except StopIteration:
	print("------------------------------------------------------------------------")
	sys.exit()
