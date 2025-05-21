#ThreadOopsEx5.py
import threading,time
class Sample1:
	def welcome(self):
		print("\tWelcome to Multi Threading--thread name=",threading.current_thread().name)
		time.sleep(5)
		print("\t{} Came-out off Sleep".format(threading.current_thread().name))
class Sample2:
	def greet(self,sname):
		print("Hi {}. Good Evening--thread name:{}".format(sname,threading.current_thread().name))
		time.sleep(5)
		print("\t{} Came-out off Sleep".format(threading.current_thread().name))
#Main Program
t1=threading.Thread(target=Sample1().welcome)
t2=threading.Thread(target=Sample2().greet,args=("Rossum",))
t1.start()
t2.start()