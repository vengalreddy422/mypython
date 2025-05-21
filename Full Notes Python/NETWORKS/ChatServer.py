#A: Write a Server Side Program in such way that It Should accept a Message from Client Side Program and give  Reply to the Client Side Program
#ChatServer.py
import socket
s=socket.socket()
s.bind(("127.0.0.1",8888))
s.listen(3)
while(True):
	csock,caddr=s.accept()
	cdata=csock.recv(1024).decode()
	print("Student-->{}".format(cdata))
	sdata=input("KVR-->")
	csock.send(sdata.encode())
