#Program for generating student marks Report
#StudentMarksReport2.py
#Accept the student number and validate
while(True):
	while(True):
		sno=input("Enter Student Number:")
		if(not sno.isdigit()):
			print("\tStudent Number should not be non-integer-try again".format(sno))
		elif(int(sno) not in range(100,201)):
			print("\t{} is Invalid Student Number-try again".format(sno))
		else:
			break
	#Accept the student Name and validate		
	while(True):
		sname=input("Enter UR name:") 
		words=sname.split() 
		if(len(words)==0):
			print("Name should not empty--try again")
		else:
			res=True
			for word in words:
				if(not word.isalpha()):
					res=False
					break
			if(not res):
				print("\t{} is Invalid Name-try again".format(sname))
			else:
				break
	#Accept the student Marks in c and validate
	while(True):
		cm=input("Enter Student Marks in C:")
		if(not cm.isdigit()):
			print("\tStudent Marks in C should not be non-integer-try again".format(cm))
		elif(int(cm) not in range(0,101)):
			print("\t{} is Invalid Student Marks in C-try again".format(cm))
		else:
			break

	#Accept the student Marks in C++ and validate
	while(True):
		cppm=input("Enter Student Marks in C++:")
		if(not cppm.isdigit()):
			print("\tStudent Marks in C++ should not be non-integer-try again".format(cppm))
		elif(int(cppm) not in range(0,101)):
			print("\t{} is Invalid Student Marks in C++-try again".format(cppm))
		else:
			break
	#Accept the student Marks in PYTHON and validate
	while(True):
		pym=input("Enter Student Marks in Python:")
		if(not pym.isdigit()):
			print("\tStudent Marks in Python should not be non-integer-try again".format(pym))
		elif(int(pym) not in range(0,101)):
			print("\t{} is Invalid Student Marks in Python-try again".format(pym))
		else:
			break
	#Calculate Total Marks and Percentage of Marks
	totmarks=int(cm)+int(cppm)+int(pym)
	percent=(totmarks/300)*100
	#If Student Secure less than 40 in any one of the subject then grade="FAIL"
	if(int(cm)<40) or(int(cppm)<40) or (int(pym)<40):
		grade="FAIL"
	else:
		if(totmarks in range(250,301)):
			grade="DISTINCTION"
		elif(totmarks in range(200,250)):
			grade="FIRST"
		elif(totmarks in range(150,200)):
			grade="SECOND"
		elif(totmarks in range(120,150)):
			grade="THIRD"
	#Display Student Marks Report
	print("*"*50)
	print("\t\tSTUDENT MARKS REPORT")
	print("*"*50)
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Marks in C:{}".format(cm))
	print("\tStudent Marks in C++:{}".format(cppm))
	print("\tStudent Marks in Python:{}".format(pym))
	print("\tStudent Total Marks :{}".format(totmarks))
	print("\tStudent Percentage of Marks :{}".format(percent))
	print("\tStudent Grade : {}".format(grade))
	print("*"*50)
	sl=[]
	sl.append(sno)
	sl.append(sname)
	sl.append(cm)
	sl.append(cppm)
	sl.append(pym)
	sl.append(totmarks)
	sl.append(percent)
	sl.append(grade)
	print("Student Data in List=",sl)

	ch=input("Do u want to Enter another Student Data(yes/no):")
	if(ch.lower()=="no"):
		print("Thx for using project")
		break


