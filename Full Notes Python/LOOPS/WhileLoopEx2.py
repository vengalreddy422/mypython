#Program for Generating N to 1 where N is +ve
#WhileLoopEx2.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("=" * 50)
    print("Number from {} to 1".format(n))
    print("=" * 50)
    i=n # Initlization Part
    while(i>0): # Cond Part
        print("\t{}".format(i))
        i=i-1 # Updation Part
    else:
        print("="*50)
