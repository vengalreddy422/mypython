#Program for Creating  Sub Thread
#JoinSubThreadsEx1.py
import threading,time
def welcome():
	print("\tWelcome to Multi Threading--thread name=",threading.current_thread().name)
	time.sleep(5)
	print("\t{} Came-out off Sleep".format(threading.current_thread().name))

def greet(sname):
	print("Hi {}. Good Evening--thread name:{}".format(sname,threading.current_thread().name))
	time.sleep(5)
	print("\t{} Came-out off Sleep".format(threading.current_thread().name))

#Main Program
print("Program Executed Started: Thread Name:{}".format(threading.current_thread().name))
print("Initially,Number of Sub Threads=",threading.active_count())
#Create 2 Sub Threads
t1=threading.Thread(target=welcome)
t2=threading.Thread(target=greet,args=("Rossum",) )
print("Execution Status of t1 before start=",t1.is_alive())
print("Execution Status of t2 before satrt=",t2.is_alive())
#dispatch the sub threads
t1.start()
t2.start()
print("Number of Sub Threads during sub threads Execution =",threading.active_count())
print("Execution Status of t1 after start=",t1.is_alive())
print("Execution Status of t2 after start=",t2.is_alive())
#Join the Sub threads
t1.join()
t2.join()
print("Number of Sub Threads after joining (completion)=",threading.active_count())
print("Program Executed Ended: Thread Name:{}".format(threading.current_thread().name))