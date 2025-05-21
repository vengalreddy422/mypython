#PureKeywordVarLengthArgsEx4.py
def findtotalmarks(sno,sname,cls,city="HYD",**submarks):
	print("-"*50)
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Class:{}".format(cls))
	print("\tStudent City:{}".format(city))
	print("-"*50)
	totmarks=0
	print("\tSubjects\tMarks")
	print("-"*50)
	for subject,marks in submarks.items():
		print("\t{}\t\t{}".format(subject,marks))
		totmarks=totmarks+marks
	print("\t\tTOTAL MARKS:{}".format(totmarks))
	print("-"*50)



#Main Program
findtotalmarks(10,"RS","X",Telugu=60,Hindi=80,English=89,Maths=90,Scienec=78,Social=89)
findtotalmarks(20,"TR","XII",Sankrit=99,Eng=89,Maths=75,Physics=60,Chemistry=59)
findtotalmarks(30,"JH","B.Tech",OS=78,DBMS=56,NW=54)
findtotalmarks(40,"SS","Rsearch")
findtotalmarks(50,"DT","Politics",Eco=56,His=45,Civ=67,city="USA")
findtotalmarks(40,"SR","Research","AUS")