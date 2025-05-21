#Program for Dead Lock Elimination
#DeadLockEliminateOopEx3.py
import threading,time
class MulTable:
	#Create an Object of Lock Class of threading module
	L=threading.Lock() # Step-1--Here L is called Class Level Data Member
	def __init__(self,n):
		self.n=n
	def table(self):
		#Get the Lock--Step-2
		MulTable.L.acquire()
		if(self.n<=0):
			print("{}-->{} Invalid Input".format(threading.current_thread().name,self.n))
		else:
			for i in range(1,11):
				print("\t{}--->{} x {} = {}".format(threading.current_thread().name,self.n,i,self.n*i))
				time.sleep(0.01)
		print("---------------------------------------------------------")
		#Release the Lock-Step-3
		MulTable.L.release() 
#Main Program

#Create Multiple Threads with Same target Functions 
t1=threading.Thread(target=MulTable(-17).table)
t1.name="RS"
t2=threading.Thread(target=MulTable(7).table)
t2.name="TR"
t3=threading.Thread(target=MulTable(-19).table)
t3.name="JH"
t4=threading.Thread(target=MulTable(18).table)
t4.name="DR"
#dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()
