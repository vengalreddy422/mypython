#Program for Generating 1 to N Numbers, where N is +ve
#WhileLoopEx1.py
n=int(input("Enter How Many Numbers u want to Generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    i=1 # Initlization Part
    while(i<=n): # Cond Part
        print("\t{}".format(i))
        i+=1 # Updation Part
    else:
        print("I am from Else Part of while loop")
    print("Program Execution Completed!")
