#Program for finding Squares for Every Value of List
#MapEx2.py
print("Enter List of Values  Separated by Space")
lst=[float(val) for val in input().split()]
sqlist=list(map(lambda val:val**2,lst))
print("----------------------------------")
print("Given Numbers\t\tSquares")
print("----------------------------------")
for gn,sqv in zip(lst,sqlist):
    print("\t{}\t\t\t\t{}".format(gn,sqv))
print("----------------------------------")
