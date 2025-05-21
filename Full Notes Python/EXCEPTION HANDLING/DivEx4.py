#Program for Demonstrating the Need of Exceotion Handling
#Cal Div of Two Numbers
#DivEx4.py
try:
	print("Program Execution Started")
	s1=input("Enter First value:")
	s2=input("Enter Second value:")
	#Convert str values into int type
	a=float(s1)   
	b=float(s2)   
	#Cal Div
	c=a/b 
except ZeroDivisionError as k:
	print("\t",k)
except ValueError as v:
	print("\t",v)
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




	