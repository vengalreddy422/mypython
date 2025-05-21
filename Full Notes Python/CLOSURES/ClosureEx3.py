#ClosureEx3.py
import time
def  gethours():
	hr=6 # Local Variable in Outer Function
	def getmins(): # Inner Function
		for m in range(1,60):
			print("\t{}:{}PM".format(hr,m))
			time.sleep(0.25)
	return getmins

#Main Program
gm=gethours() # Outer Function call
gm()


