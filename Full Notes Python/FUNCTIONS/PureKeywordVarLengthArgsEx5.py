#PureKeywordVarLengthArgsEx5.py
def findtotalmarks(sno,sname,cls,*intmarks,city="HYD",**submarks):
	print("-"*50)
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Class:{}".format(cls))
	print("\tStudent City:{}".format(city))
	im=0
	print("\tInternal Marks")
	for m in intmarks:
		print("\t{}".format(m))
		im=im+m
	print("-"*50)
	em=0
	print("\tSubjects\tMarks")
	print("-"*50)
	for subject,marks in submarks.items():
		print("\t{}\t\t{}".format(subject,marks))
		em=em+marks
	print("Internal Marks:{} \t External Marks:{}".format(im,em))
	print("\t\tTOTAL MARKS:{}".format(im+em))
	print("-"*50)



#Main Program
findtotalmarks(10,"RS","X",10,15,17,18,12,18,Telugu=60,Hindi=80,English=89,Maths=90,Scienec=78,Social=89)
findtotalmarks(20,"TR","XII",18,12,11,12,18,Sankrit=99,Eng=89,Maths=75,Physics=60,Chemistry=59)
findtotalmarks(30,"JH","B.Tech",2.3,4.5,5.6,OS=78,DBMS=56,NW=54)
findtotalmarks(40,"SS","Rsearch",1,2,3)
findtotalmarks(50,"DT","Politics",Eco=56,His=45,Civ=67,city="USA")
findtotalmarks(40,"SR","Research",city="AUS")