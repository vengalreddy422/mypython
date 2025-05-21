#B. Write a Client Side Program in such way that It should accept a Message from Key Board , Send to Server Side  Program and Obtain Its Reply 
#ChatClient.py
import socket
while(True):
	s=socket.socket()
	s.connect(("127.0.0.1",8888))
	cdata=input("Student-->")
	if(cdata.lower()=="bye"):
			s.send(cdata.encode())
			break
	else:
		s.send(cdata.encode())
		sdata=s.recv(1024).decode()
		print("KVR-->{}".format(sdata))