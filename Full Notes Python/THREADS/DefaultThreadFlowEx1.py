#Program for Demonstrating Default Thread Flow with Functions
#DefaultThreadFlowEx1.py
import threading
def welcome():
	print("\t5:welcome()--executed by:{}".format(threading.current_thread().name))
def hello():
	print("\t7:hello()--executed by:{}".format(threading.current_thread().name))
def hi():
	print("\t9:hi()--executed by:{}".format(threading.current_thread().name))

#Main Program
print("12:---------------------------------------------------------------------------------")
print("13:Program Execution Started by :{}".format(threading.current_thread().name))
print("Line:14")
welcome()
print("Line:16")
hello()
print("Line:18")
hi()
print("Line:20")
print("---------------------------------------------------------------------------------")
print("Program Execution Ended by :{}".format(threading.current_thread().name))
print("---------------------------------------------------------------------------------")