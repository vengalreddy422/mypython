#Program for Demonstrating Default Thread Flow with Functions
#SubThreadsFlowEx1.py
import threading,time
def welcome():
	print("\t5:welcome()--executed by:{}".format(threading.current_thread().name))
	time.sleep(3)
def hello():
	print("\t7:hello()--executed by:{}".format(threading.current_thread().name))
	time.sleep(3)
def hi():
	print("\t9:hi()--executed by:{}".format(threading.current_thread().name))
	time.sleep(3)
#Main Program
print("12:---------------------------------------------------------------------------------")
print("13:Program Execution Started by :{}".format(threading.current_thread().name))
print("By Default Number of Threads=",threading.active_count())
print("14:---------------------------------------------------------------------------------")
#Create 3 Sub Threads 
t1=threading.Thread(target=welcome)  # here t1 is called Thread Object---Thread-1
t1.name="Rossum"
t2=threading.Thread(target=hello)  # here t2 is called Thread Object---Thread-2
t2.name="Travis"
t3=threading.Thread(target=hi)  # here t3 is called Thread Object---Thread-3
t3.name="HUnter"
#Dispatch the sub threads
t1.start()
t2.start()
t3.start()
print("Programatically Number of Threads=",threading.active_count())
t1.join()
t2.join()
t3.join()
print("Programatically Number of Threads after completion=",threading.active_count())
print("---------------------------------------------------------------------------------")
print("Program Execution Ended by :{}".format(threading.current_thread().name))
print("---------------------------------------------------------------------------------")