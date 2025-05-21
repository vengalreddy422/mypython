#Program for Dead Lock Elimination
#TrainReservationOopEx1.py
import threading,time
class Train:
	lockobj=threading.Lock()
	totseats=12
	def __init__(self,seats):
		self.seats=seats
	def  reservation(self):
		Train.lockobj.acquire()
		if(self.seats>Train.totseats):
			print("\t Dear Passenger {},  {} Seats Not Available--Try Next".format(threading.current_thread().name,self.seats))
			time.sleep(3)
		else:
			Train.totseats=Train.totseats-self.seats
			print("\t Dear Passenger {},  {} Seats Reserved--hpy jrny ".format(threading.current_thread().name,self.seats))
			time.sleep(3)
			print("\tNow Available Seats:{}".format(Train.totseats))
			time.sleep(3)
		Train.lockobj.release()

#Main Program
t1=threading.Thread(target=Train(15).reservation)
t1.name="Sasi"
t2=threading.Thread(target=Train(2).reservation)
t2.name="Sai"
t3=threading.Thread(target=Train(4).reservation)
t3.name="Chran"
t4=threading.Thread(target=Train(8).reservation)
t4.name="Prajwal"
t5=threading.Thread(target=Train(4).reservation)
t5.name="Moula"
t6=threading.Thread(target=Train(2).reservation)
t6.name="Meghna"
t7=threading.Thread(target=Train(1).reservation)
t7.name="pavan"
#Dispatch the Threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
