#ThreadOopsEx4.py
import threading,time # Step-1
class Greet:#Step-2
	def __init__(self,sname):
		self.sname=sname
	def welcome(self): # Step-3--Instance Method
		print("Hi:{},Welcome to Multi Threading".format(self.sname))


#Main Program
threading.Thread(target=Greet("Rossum").welcome) .start() # step4-& Step-5
