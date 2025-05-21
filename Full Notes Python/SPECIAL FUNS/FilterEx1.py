#Program for Filtering +ve Values from List of Values
#FilterEx1.py
def pos(val):
    if(val>0):
        return True
    else:
        return False
#main Program
print("Enter List of Values  Separated by Space")
lst=[float(val) for val in input().split()]
x=filter(pos,lst) # here pos is a normal function
# Here x is an object of <class 'filter'> and convert it into list type
pslist=list(x)
print("Given List of Values=",lst)
print("+Ve Values=",pslist)
