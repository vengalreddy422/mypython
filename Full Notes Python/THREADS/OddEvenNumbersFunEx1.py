#Program for generatng Odd and Even Number by Multiple Threads
#OddEvenNumbersFunEx1.py
import threading,time
def  odd(n):
	if(n<=0):
		print("{}-->{} Invalid Input".format(threading.current_thread().name,n))
	else:
		for i in range(1,n+1,2):
			print("{}--->Odd Number:{}".format(threading.current_thread().name,i))
			time.sleep(0.5)
		print("-----------------------------------------------------------")
def even(n):
		if(n<=0):
			print("{}-->{} Invalid Input".format(threading.current_thread().name,n))
		else:
			for i in range(2,n+1,2):
				print("{}--->Even Number:{}".format(threading.current_thread().name,i))
				time.sleep(0.5)
			print("-----------------------------------------------------------")

#Main Program
#Create 2 Threads 
t1=threading.Thread(target=odd,args=(int(input("Enter How Many Odd Numbers u want to generate:")),))
t2=threading.Thread(target=even,args=(int(input("Enter How Many Even Numbers u want to generate:")),))
#dispatch the sub threads
t1.start()
t2.start()