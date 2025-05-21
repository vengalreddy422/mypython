#Program for Demonstrating generator
#GenEx5.py
def  kvrrange(Start,Stop,Step):
	while(Start<=Stop):
		yield Start
		Start=Start+Step


#Main Program
x=kvrrange(10,20,2)
for val in x:
	print("\t{}".format(val))