#Program for Dead Lock Elimination
#BankTransactionOopEx1.py
import threading,time
class Bank:
	lockobj=threading.Lock()
	VMACC=2500
	def __init__(self,chamt):
		self.chamt=chamt
	def  clearence(self):
		Bank.lockobj.acquire()
		if(self.chamt>Bank.VMACC):
			print("\t Dear Customer {}, INR {} Check Bounced--Contact Source".format(threading.current_thread().name,self.chamt))
			time.sleep(3)
		else:
			Bank.VMACC=Bank.VMACC-self.chamt
			print("\t Dear Customer {}, INR {} Check Cleared".format(threading.current_thread().name,self.chamt))
			time.sleep(3)
			print("\tNow Available Balance at Source:{}".format(Bank.VMACC))
			time.sleep(3)
		Bank.lockobj.release()


#Main Program
t1=threading.Thread(target=Bank(5000).clearence)
t1.name="Mansi"
t2=threading.Thread(target=Bank(2000).clearence)
t2.name="Uma"
t3=threading.Thread(target=Bank(4000).clearence)
t3.name="Namtritha"
t4=threading.Thread(target=Bank(2500).clearence)
t4.name="Bargavi"
t5=threading.Thread(target=Bank(10000).clearence)
t5.name="Pallavi"
t6=threading.Thread(target=Bank(500).clearence)
t6.name="Kvr"
t7=threading.Thread(target=Bank(1500).clearence)
t7.name="Srinu"
#Dispatch the Threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
