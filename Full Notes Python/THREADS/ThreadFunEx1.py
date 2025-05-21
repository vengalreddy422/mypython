#ThreadFunEx1.py
import threading,time # Step-1
def welcome(sname): # Step-2
	print("Hi:{},Welcome to Multi Threading".format(sname))
#Main Program
t1=threading.Thread(target=welcome,args=("Rossum",)) # Step-3
t1.start() # Step-4
