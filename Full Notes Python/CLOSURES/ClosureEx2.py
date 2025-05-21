#ClosureEx2.py
def icicibankloanprocess(processingfee): #Outer Function OR Enclosing Function
	def  iciciemical(emiamt): # Inner Function OR Enclosed Function
		finalemi=processingfee+emiamt
		return finalemi
	return iciciemical

#Main Program
iciciem=icicibankloanprocess(100) # Outer Function call
emipay=iciciem(10000) # Inner Function Call
print("Pay=",emipay)
emipay=iciciem(15000) # Inner Function Call
print("Pay=",emipay)
