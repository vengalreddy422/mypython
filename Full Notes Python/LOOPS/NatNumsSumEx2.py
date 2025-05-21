#Program for Finding the sum of N Natural Numbers
#NatNumsSumEx1.py
n=int(input("Enter How Many Natural Numbers Squares and Cubes sum u want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    s,ss,cs=0,0,0
    print("-" * 50)
    print("\tNatNums\t\tSquares\t\t\tCubes")
    print("-" * 50)
    for i in range(1,n+1):
        print("\t{}\t\t\t\t{}\t\t\t{}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("-"*50)
        print("\t{}\t\t\t\t{}\t\t\t{}".format(s,ss,cs))
        print("-" * 50)
