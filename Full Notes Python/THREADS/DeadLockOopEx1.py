#Program for Dead Lock Occurence
#DeadLockOopEx1.py
import threading,time
class MulTable:
	def table(self,n):
		if(n<=0):
			print("{}-->{} Invalid Input".format(threading.current_thread().name,n))
		else:
			for i in range(1,11):
				print("\t{}--->{} x {} = {}".format(threading.current_thread().name,n,i,n*i))
				time.sleep(1)
			print("---------------------------------------------------------")

#Main Program
t1=threading.Thread(target=MulTable().table,args=(17,))
t1.name="RS"
t2=threading.Thread(target=MulTable().table,args=(7,))
t2.name="TR"
t3=threading.Thread(target=MulTable().table,args=(-19,))
t3.name="JH"
t4=threading.Thread(target=MulTable().table,args=(18,))
t4.name="DR"
#dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()
