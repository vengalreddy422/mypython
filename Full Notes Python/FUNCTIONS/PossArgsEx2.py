#Program for Demonstrating Posstional Arguments
#PossArgsEx2.py
def dispstudinfo(sno,sname,marks,crs):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))



#Main Program
print("-"*60)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("-"*60)
dispstudinfo(10,"RS",34.56,"PYTHON") # Function Call 
dispstudinfo(20,"TR",67.89,"PYTHON") # Function Call 
dispstudinfo(30,"DR",37.89,"PYTHON") # Function Call 
dispstudinfo(40,"SS",17.19,"PYTHON") # Function Call 
dispstudinfo(50,"KV",45.67,"PYTHON") # Function Call 
print("-"*60)