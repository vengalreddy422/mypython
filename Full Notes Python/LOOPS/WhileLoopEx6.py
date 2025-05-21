#Program for Generating Mul Table for N where n is +Ve
#WhileLoopEx6.py
n=int(input("Enter a Number for Generating Mul Table:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    print("="*50)
    print("Mul Table for :{}".format(n))
    print("=" * 50)
    i=1
    while(i<=10):
        print("\t{} x {} = {}".format(n,i,n*i))
        i=i+1
    else:
        print("=" * 50)