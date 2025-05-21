#CurrentThreadEx1.py
import threading
t=threading.current_thread()
print("Default Name of therad=",t.name)
print("-----------------------OR----------------------")
print("Default Name of therad=",threading.current_thread().name)
