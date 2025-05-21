#Program for Validating Mobile Number by using Reg Expr.
#MobileNumberValidationEx1.py
import re
while(True):
	mno=input("Enter Ur Mobile Number:")
	if(len(mno)==10):
		res=re.search(r"\d{10}",mno)
		if(res!=None):
			print("\t{} Mobile Number is Valid:".format(mno))
			break
		else:
			print("\t{} Mobile Number Should Not Contain non-ints--try again:".format(mno))
	else:
		print("\t{} is invalid Mobile Number Length-try again".format(mno))