#Program for Generating All Even Numbers within N where n is +ve
#WhileLoopEx4.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("="*50)
    print("Even Numbers within:{}".format(n))
    i=2 # Initlization Part
    while(i<=n): # Cond Part
        print("\t\t{}".format(i))
        i=i+2 # Updation Part
    else:
        print("=" * 50)

