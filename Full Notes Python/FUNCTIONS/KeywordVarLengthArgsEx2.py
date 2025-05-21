#Program for Demonstrating   Keyword Variable Length Arguments
#NOTE: This Program will Execute as It is 
#KeywordVarLengthArgsEx2.py
def disp(sno,sname,marks):#Function Def-1
	print(sno,sname,marks)
disp(sno=10,sname="RS",marks=45.67) # Function call-1 with 3 Keyword variable  length Args
#-----------------------------------------------------------------------------------------------------
def disp(tno,tname,sub1,sub2): #Function Def-2
	print(tno,tname,sub1,sub2)

disp(tno=100,tname="TR",sub1="Python",sub2="Java") # Function call-2 with 4 Keyword variable  length Args
#-----------------------------------------------------------------------------------------------------
def disp(cid,cname,hb1,hb2,hb3): #Function Def-3
	print(cid,cname,hb1,hb2,hb3)

disp(cid=200,cname="DR",hb1="Eating",hb2="Sleeping",hb3="Chating") # Function call-3 with 5 Keyword variable  length Args
#-----------------------------------------------------------------------------------------------------

