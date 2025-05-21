#Program for finding Squares for Every Value of List
#MapEx3.py
print("Enter List of Values  Separated by Space")
lst=[float(val) for val in input().split()]
sqlist=list(map(lambda val:val**2,lst))
sqrtlist=list(map(lambda val:val**0.5,lst))
print("-------------------------------------------------")
print("Given Numbers\t\tSquares\t\tSquareRoot")
print("-------------------------------------------------")
for gn,sqv,sqt in zip(lst,sqlist,sqrtlist):
    print("\t{}\t\t\t\t{}\t\t{}".format(gn,sqv,round(sqt,2)))
print("------------------------------------------------")
