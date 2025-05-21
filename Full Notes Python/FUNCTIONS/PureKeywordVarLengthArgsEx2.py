#Program for Demonstrating   Keyword Variable Length Arguments
#NOTE: This Program will Execute as It is 
#PureKeywordVarLengthArgsEx2.py

def  disp(**kvr): # Here **kvr is called Kwd Var length param and whose is type dict
	print("-"*50)
	for k in kvr.keys():
		print("\t{}--->{}".format(k,kvr[k]))
	print()
	print("-"*50)

#Main Program---Family of Similar Functions with Keyword variable  length Args
disp(sno=10,sname="RS",marks=45.67) # Function call-1 with 3 Keyword variable  length Args
disp(tno=100,tname="TR",sub1="Python",sub2="Java") # Function call-2 with 4 Keyword variable  length Args
disp(cid=200,cname="DR",hb1="Eating",hb2="Sleeping",hb3="Chating") # Function call-3 with 5 Keyword variable  length Args