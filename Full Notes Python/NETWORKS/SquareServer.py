#A.  Write a Server Side Program in such way that It Should accept a Number a From Client Side Program, Square It  and Gives the Result to Client Side Program 
#SquareServer.py
import socket # Step-1
s=socket.socket() # Step-2
s.bind(("localhost",9999)) # Step-3
s.listen(2)#Step-4
print("SSP is Ready to accept any CSP Request")
while(True):
	try:
		cs,ca=s.accept() # Step-5
		#Step-6
		cdata=cs.recv(1024).decode()  # Reading Client Request Data
		print("Val of Client at Server=",cdata)
		res=float(cdata)**2 # Processing the Client Request Data
		cs.send(str(res).encode())  # Gives Response back to client side program
	except ValueError:
		cs.send("Don't enter alnums,strs and symbols for Num-Value".encode())




