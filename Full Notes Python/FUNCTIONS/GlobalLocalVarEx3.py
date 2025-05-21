#Pogram for Demonstrating the Need of Local and Global Variables
#GlobalLocalVarEx3.py
lang="PYTHON" # Here lang is called Global Variable
def learnAI():
	sub1="AI"
	print("To Implement '{}' Based Applications, we  use '{}' Lang".format(sub1,lang))
	#print(sub2,sub3)---can't access, bcoz sub2 and sub3 are local to other functions

def learnML():
	sub2="ML"
	print("To Implement '{}' Based Applications, we  use '{}' Lang".format(sub2,lang))
	#print(sub1,sub3)---can't access, bcoz sub1 and sub3 are local to other functions

def learnDL():
	sub3="DL"
	print("To Implement '{}' Based Applications, we  use '{}' Lang".format(sub3,lang))
	#print(sub1,sub2)---can't access, bcoz sub1 and sub1 are local to other functions

#Main Program
learnAI()
learnML()
learnDL()