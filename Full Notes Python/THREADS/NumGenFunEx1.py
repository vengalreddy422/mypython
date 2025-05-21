#Program generating 1 to N where N is +Ve after each and every Second
#NumGenFunEx1.py
import threading,time
def generate(n):
	if(n<=0):
		print("{}-->Invalid input:{}".format(threading.current_thread().name,n))
	else:
			for val in range(1,n+1):
				print("\tValue:{}".format(val))
				time.sleep(0.25)
#Main Program
n=int(input("Enter How Many Numbers u want to Generate:"))
t1=threading.Thread(target=generate,args=(n,))
t1.start()