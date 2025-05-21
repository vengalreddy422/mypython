#Program for Demonstrating generator
#GenEx5.py
def  kvrrange(Start=1,Stop=1,Step=1):
	if(Start>Stop):
		Stop=Start
		Start=1
	
	while(Start<=Stop):
		yield Start
		Start=Start+Step

#Main Program
x=kvrrange(5)
for val in x:
	print("\t{}".format(val))
print("-----------------------------------------------------------")
y=kvrrange(10,20)
for val in y:
	print("\t{}".format(val))
print("-----------------------------------------------------------")
z=kvrrange(10,100,10)
for val in z:
	print("\t{}".format(val))
print("-----------------------------------------------------------")

