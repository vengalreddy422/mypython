#B. Write a Client Side Program in such way that It should accept a Number from Key Board , Send to Server Side Program and Obtain Its Square
#SquareClient.py
import socket # Step-1
s=socket.socket() # Step-2
s.connect(("localhost",9999)) # Step-3
print("CSP Connected with SSP")
#read the Data from Key Board
val=input("Enter a Number for Getting Its Square:")
s.send(val.encode()) # Step-4
res=s.recv(1024).decode() # # Step-5
print("Square({})={}".format(val,res))


