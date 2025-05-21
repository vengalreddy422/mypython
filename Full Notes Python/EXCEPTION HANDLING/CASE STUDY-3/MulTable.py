#MulTable.py<--File Name and Module Name
from MulExcept import ZeroError,NegativeNumberError
def table(n):
    if(n==0):
        raise ZeroError
    elif(n<0):
        raise NegativeNumberError
    else:
        print("-"*50)
        print("\tMul Table for:{}".format(n))
        print("-" * 50)
        for i in range(1,11):
            print("\t{} x {} ={}".format(n,i,n*i))
        print("-" * 50)
