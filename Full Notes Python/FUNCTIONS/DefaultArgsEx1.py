#Program for Demonstrating Default Arguments
#DefaultArgsEx1.py
def dispstudinfo(sno,sname,marks,crs="PYTHON"):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))


#Main Program
print("-"*60)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("-"*60)
dispstudinfo(10,"RS",34.56) # Function Call 
dispstudinfo(20,"TR",67.89) # Function Call 
dispstudinfo(30,"DR",37.89) # Function Call 
dispstudinfo(40,"SS",17.19) # Function Call 
dispstudinfo(50,"KV",45.67) # Function Call 
print("-"*60)