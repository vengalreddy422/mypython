#Program for List Numerical Values and Find Biggest and smallest among them
# and check for Equality
#AnonymousFunEx4.py
findlistmax=lambda lst: max(lst)
findlistmin=lambda lst: min(lst)

#Main Program
print("Enter List of Values Separated Space")
lst=[float(val) for val in input().split()]
bv=findlistmax(lst)
sv=findlistmin(lst)
print("Max({})={}".format(lst,bv))
print("Min({})={}".format(lst,sv))
