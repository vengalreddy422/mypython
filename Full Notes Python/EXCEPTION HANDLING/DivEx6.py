#Program for Demonstrating the Need of Exceotion Handling
#Cal Div of Two Numbers
# This Program/ Task Developed by KVR Programmer in 26-02-2025 and at this Point of time we have Two exceptions and we handled It. In 26-02-2030 This code may go for Modifications by the New Programer "Rishi"
#DivEx6.py
try:
	print("Program Execution Started")
	s1=input("Enter First value:")
	s2=input("Enter Second value:")
	#Convert str values into int type
	a=float(s1)   
	b=float(s2)   
	#Cal Div
	c=a/b 
	s="PYTHON"
	print(s[10])
except ZeroDivisionError:
	print("\tDON'T ENTER ZERO FOR DEN...")
except ValueError:
	print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS")
except IndexError:
	print("\tCheck Ur Index")
except: # default except--must be written last
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




	