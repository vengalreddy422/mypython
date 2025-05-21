#Program for List Numerical Values and Find Biggest and smallest among them
# and check for Equality
#AnonymousFunEx6.py
def kvrmax(lst): # Normal Function
    maxv=lst[0]
    for val in lst:
        if(val>maxv):
            maxv=val
    return maxv

def kvrmin(lst): # Normal Function
    minv=lst[0]
    for val in lst:
        if(val<minv):
            minv=val
    return minv

# Calling # Normal Function as Part of Anonymous Functions
findlistmax=lambda lst: kvrmax(lst)
findlistmin=lambda lst: kvrmin(lst)

#Main Program
print("Enter List of Values Separated Space")
lst=[float(val) for val in input().split()]
bv=findlistmax(lst)
sv=findlistmin(lst)
print("Max({})={}".format(lst,bv))
print("Min({})={}".format(lst,sv))
