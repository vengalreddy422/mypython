#Program for Demonstrating Default Arguments
#DefaultArgsEx2.py
def dispstudinfo(sno,sname,marks,crs="PYTHON",city="HYD"):
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,city))


#Main Program
print("-"*60)
print("\tSNO\tNAME\tMARKS\tCOURSE\tCITY")
print("-"*60)
dispstudinfo(10,"RS",34.56) # Function Call 
dispstudinfo(20,"TR",67.89) # Function Call 
dispstudinfo(30,"DR",37.89) # Function Call 
dispstudinfo(40,"SS",17.19) # Function Call 
dispstudinfo(50,"KV",45.67) # Function Call 
dispstudinfo(60,"DT",22.22,city="USA") # Function Call 
dispstudinfo(70,"PT",32.22,city="RSA",crs="JAVA") # Function Call 
dispstudinfo(crs="HTML",marks=34.56,city="AUS",sno=80,sname="SS")
print("-"*60)