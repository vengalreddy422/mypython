#B.Write a Client Side Program in such way that It should accept an employee Number from Key Board , Send to Server Side Program and Obtain Other Deatils of Employee
#DataBaseClient.py
import socket
s=socket.socket()
s.connect(("localhost",3600))
print("CSP Connected with SSP")
empno=input("Enter Employee Number for Getting Other Deatils:")
s.send(empno.encode())
record=s.recv(1024).decode()
print("Result from Server")
print(record)
