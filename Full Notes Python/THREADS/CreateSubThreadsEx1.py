#Program for Creating  Sub Thread
#CreateSubThreadsEx1.py
import threading,time
def welcome():
	print("Welcome to Multi Threading--thread name=",threading.current_thread().name)
	time.sleep(2)

def greet(sname):
	print("Hi {}. Good Evening--thread name:{}".format(sname,threading.current_thread().name))
	time.sleep(2)

#Main Program
t1=threading.Thread(target=welcome)
t2=threading.Thread(target=greet,args=("Rossum",) )
print("Execution Status of t1=",t1.is_alive())
print("Execution Status of t2=",t2.is_alive())
#dispatch the sub threads
t1.start()
t2.start()
print("Number of Sub Threads=",threading.active_count())
print("Execution Status of t1=",t1.is_alive())
print("Execution Status of t2=",t2.is_alive())