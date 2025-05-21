#Program for Creating  Sub Thread
#SetGetSubThreadNamesEx1.py
import threading,time
def welcome():
	print("Welcome to Multi Threading--thread name=",threading.current_thread().name)

def greet(sname):
	print("Hi {}. Good Evening--thread name:{}".format(sname,threading.current_thread().name))

#Main Program
t1=threading.Thread(target=welcome)
t2=threading.Thread(target=greet,args=("Rossum",) )
#print("Default Name of Sub Thread1=",t1.getName())--Not recommended to use
#print("Default Name of Sub Thread2=",t2.getName())--Not recommended to use
print("Default Name of Sub Thread1=",t1.name)
print("Default Name of Sub Thread2=",t2.name)
#Set the Names to Sub Threads
#t1.setName("RS")---Not recommended to use
#t2.setName("TR")---Not recommended to use
t1.name="RS"
t2.name="TR"
print("User-Freindly  Name of Sub Thread1=",t1.name)
print("User-Freindly  of Sub Thread2=",t2.name)

