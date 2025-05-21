#ThreadOopsEx1.py
import threading,time # Step-1
class Greet:#Step-2
	def welcome(self,sname): # Step-3--Instance Method
		print("Hi:{},Welcome to Multi Threading".format(sname))


#Main Program
go=Greet() # Create create Greet Class for welcome() w.r.t  'go' by the sub thread
t1=threading.Thread(target=go.welcome,args=("Rossum",)) # Step-4
t1.start() # Step-5
