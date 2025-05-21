#ThreadOopsEx3.py
import threading,time # Step-1
class Greet:#Step-2
	def __init__(self,sname):
		self.sname=sname
	def welcome(self): # Step-3--Instance Method
		print("Hi:{},Welcome to Multi Threading".format(self.sname))


#Main Program
t1=threading.Thread(target=Greet("Rossum").welcome) # Step-4
t1.start() # Step-5
