#Python Program shows the execution of MainThread Only
#DefaultThreadFlowwithTimeEx1.py
import threading,time
def squares(lst):
	for val in lst:
		print("\t{}-->Square({})={}".format(threading.current_thread().name,val,val**2))
		time.sleep(1)

def cubes(lst):
		for val in lst:
			print("\t{}-->cube({})={}".format(threading.current_thread().name,val,val**3))
			time.sleep(1)

#Main Program
bt=time.time()
print("---------------------------------------------------------------------------------")
print("Program Execution Started by :{}".format(threading.current_thread().name))
print("---------------------------------------------------------------------------------")
lst=[12,17,4,5,-5,18,14,25,15]
squares(lst)
print("---------------------------------------------------------------------------------")
cubes(lst)
print("---------------------------------------------------------------------------------")
print("Program Execution Started by :{}".format(threading.current_thread().name))
print("---------------------------------------------------------------------------------")
et=time.time()
print("Total Execution of this Program by using default thread only=",(et-bt))