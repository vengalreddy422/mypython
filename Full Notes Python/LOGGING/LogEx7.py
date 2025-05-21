#LogEx7.py
import logging
def divop(a,b):
	if(b==0):
		logging.basicConfig(filename="E:\\KVR-PYTHON-6PM\\LOGGING\\NOTES\\error.data",level="ERROR",format='%(asctime)s  : %(levelname)s: %(message)s',datefmt='%d-%m-%Y  %I:%M:%S %p ')
		logging.error("Don't Enter Zero For Deno a={} b={}...take Care".format(a,b))
		print("ERROR written to log file")
	else:
		logging.critical("Done Well")
		logging.error("Result="+str(a/b))
		print("Div={}".format(a/b))

#Main Program
print("Program exectuion started")
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
divop(a,b)
print("Program exectuion completed")