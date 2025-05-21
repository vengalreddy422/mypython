#Program for finding Squares for Every Value of List
#MapEx1.py
def squares(val):
    return val**2

#Main Program
print("Enter List of Values  Separated by Space")
lst=[float(val) for val in input().split()]
mo=map(squares,lst)
#Here mo is an object of <class 'map'>
#Convert map object into list type
sqlist=list(mo)
print("----------------------------------")
print("Given Numbers\t\tSquares")
print("----------------------------------")
for gn,sqv in zip(lst,sqlist):
    print("\t{}\t\t\t\t{}".format(gn,sqv))
print("----------------------------------")
