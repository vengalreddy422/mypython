#Program for Dead Lock Elimination
#DeadLockEliminateFunEx1.py
import threading,time
def table(n):
	#Get the Lock--Step-2
	L.acquire()
	if(n<=0):
		print("{}-->{} Invalid Input".format(threading.current_thread().name,n))
	else:
		for i in range(1,11):
			print("\t{}--->{} x {} = {}".format(threading.current_thread().name,n,i,n*i))
			time.sleep(0.01)
	print("---------------------------------------------------------")
	#Release the Lock-Step-3
	L.release() 
#Main Program
#Create an Object of Lock Class of threading module
L=threading.Lock() # Step-1
#Create Multiple Threads with Same target Functions 
t1=threading.Thread(target=table,args=(17,))
t1.name="RS"
t2=threading.Thread(target=table,args=(7,))
t2.name="TR"
t3=threading.Thread(target=table,args=(-19,))
t3.name="JH"
t4=threading.Thread(target=table,args=(18,))
t4.name="DR"
#dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()
