#Program for Accepting the Digit and Display Its name
#IfElseStmtEx3py
d=int(input('Enter a Digit:')) # d=0 1 2 3 4 5 6 7 8 9
if(d==0):
    print("{} is ZERO".format(d))
else:
    if(d==1):
        print("{} is ONE".format(d))
    else:
        if (d == 2):
            print("{} is TWO".format(d))
        else:
            if (d == 3):
                print("{} is THREE".format(d))
            else:
                if (d == 4):
                    print("{} is FOUR".format(d))
                else:
                    if (d == 5):
                        print("{} is FIVE".format(d))
                    else:
                        if (d == 6):
                            print("{} is SIX".format(d))
                        else:
                            if (d == 7):
                                print("{} is SEVEN".format(d))
                            else:
                                if (d == 8):
                                    print("{} is EIGHT".format(d))
                                else:
                                    if (d == 9):
                                        print("{} is NINE".format(d))
                                    else:
                                        if (d > 9):
                                            print("{} is a Number:".format(d))
                                        else:
                                            if (d < 0) and d not in [-1, -2, -3, -4, -5, -6, -7, -8, -9]:
                                                print("{} is -Ve Number:".format(d))
                                            else:
                                                print("{} is -VE Digit".format(d))
print("Program Execution Completed")