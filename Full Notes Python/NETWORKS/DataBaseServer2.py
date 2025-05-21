#A. Write a Server Side Program in such way that  It Should accept an Employee Number from Client Side Program  and gives Other Details of employee by extracting from Employee Table
#DataBaseServer2.py
import socket
import oracledb as orc
s=socket.socket()
s.bind(("localhost",3600))
s.listen(2)
print("SSP is ready to accept any CSP request")
while(True):
	try:
		cs,ca=s.accept()
		cdata=cs.recv(1024).decode()
		print("Employee Number at Server={}".format(cdata))
		empno=int(cdata)
		#We must write PDBC Code 
		con=orc.connect("system/tiger@localhost/orcl")
		cur=con.cursor()
		cur.execute("select * from employee where eno=%d" %empno)
		record=cur.fetchone()
		if(record!=None):
			s1="---------------------------------------------------"
			s2="Employee Number:{}".format(record[0])
			s3="Employee Name:{}".format(record[1])
			s4="Employee Salary:{}".format(record[2])
			s5="Employee Comp Name:{}".format(record[3])
			s6="---------------------------------------------------"
			res=s1+"\n"+s2+"\n"+s3+"\n"+s4+"\n"+s5+"\n"+s6
			cs.send(res.encode())
		else:
			cs.send(("Employee Number {} Does not  Exist".format(empno)).encode() )
	except ValueError:
		cs.send("Don't enter alnums,strs and symbols for emp number".encode())
	except orc.DatabaseError as db:
		cs.send(("Problem in Oracle DataBase:"+db).encode())