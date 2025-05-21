#Program for Demonstrating Posstional Arguments
#PossArgsEx1.py
def dispstudinfo(sno,sname,marks):
	print("\t{}\t{}\t{}".format(sno,sname,marks))



#Main Program
print("-"*40)
print("\tSNO\tNAME\tMARKS")
print("-"*40)
dispstudinfo(10,"RS",34.56) # Function Call 
dispstudinfo(20,"TR",67.89) # Function Call 
dispstudinfo(30,"DR",37.89) # Function Call 
dispstudinfo(40,"SS",17.19) # Function Call 
dispstudinfo(50,"KV",45.67) # Function Call 
print("-"*40)