#Program for Demonstrating Default Thread
#DefaultThreadNameEx1.py
import threading
tname=threading.current_thread().name
print("Default Thread Name =",tname)
print("Number of Threads by Default =",threading.active_count())