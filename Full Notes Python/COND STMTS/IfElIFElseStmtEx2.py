#Program for Accepting the Digit and Display Its name
#IfElIFElseStmtEx2.py
d=int(input('Enter a Digit:')) # d=0 1 2 3 4 5 6 7 8 9
if(d==0):
    print("{} is ZERO".format(d))
elif(d==1):
    print("{} is ONE".format(d))
elif(d==2):
    print("{} is TWO".format(d))
elif(d==3):
    print("{} is THREE".format(d))
elif(d==4):
    print("{} is FOUR".format(d))
elif(d==5):
    print("{} is FIVE".format(d))
elif(d==6):
    print("{} is SIX".format(d))
elif(d==7):
    print("{} is SEVEN".format(d))
elif(d==8):
    print("{} is EIGHT".format(d))
elif(d==9):
    print("{} is NINE".format(d))
elif(d>9):
    print("{} is a Number:".format(d))
elif(d<0) and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("{} is -Ve Number:".format(d))
elif d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("{} is -VE Digit".format(d))
print("Program Execution is completed")