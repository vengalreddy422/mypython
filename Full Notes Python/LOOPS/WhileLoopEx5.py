#Program for Generating All Even Numbers within N where n is +ve
#WhileLoopEx5.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("="*50)
    print("Even Numbers within:{}".format(n))
    i=1
    while(i<=n):
        if(i%2==0):
            print("\t{}".format(i))
        i=i+1
    else:
        print("=" * 50)

