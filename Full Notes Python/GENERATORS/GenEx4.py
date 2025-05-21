#Program for Demonstrating generator
#GenEx4.py
def  kvrrange(Start,Stop):
	while(Start<=Stop):
		yield Start
		Start=Start+1


#Main Program
x=kvrrange(10,16)
print("type of kvrrange=",type(kvrrange)) # <class, 'function'>
print("Type of x=",type(x)) # <class,'generator'>
print("------------------------------------------------------------------------")
#To get the Values from generator--we must make request by using a Function called next(generatorobj)
for val in x:
	print("\t{}".format(val))
print("------------------------------------------------------------------------")
y=kvrrange(100,110)
print("type of kvrrange=",type(kvrrange)) # <class, 'function'>
print("Type of y=",type(y)) # <class,'generator'>
print("------------------------------------------------------------------------")
#To get the Values from generator--we must make request by using a Function called next(generatorobj)
for val in y:
	print("\t{}".format(val))
print("------------------------------------------------------------------------")

	
