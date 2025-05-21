#Program for Demonstrating the Need of Exceotion Handling
#Cal Div of Two Numbers
#DivEx3.py
try:
	print("Program Execution Started")
	s1=input("Enter First value:")
	s2=input("Enter Second value:")
	#Convert str values into int type
	a=float(s1)   
	b=float(s2)   
	#Cal Div
	c=a/b 
except (ZeroDivisionError,ValueError):
	print("\tDON'T ENTER ZERO FOR DEN...")
	print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS")
except BaseException: # here 'BaseException' is the super Class for all the exceptions.
	print("\tOoooops, Some thing went-wrong!!")
else:
	print("-------------else-----------------")
	print("\tVal of a:",a)
	print("\tVal of b:",b)
	print("\tDiv=",c)
	print("-----------------------------------")
finally:
	print("--------------finally-----------------------")
	print("\tProgram Execution Completed")
	print("---------------------------------------------")




	