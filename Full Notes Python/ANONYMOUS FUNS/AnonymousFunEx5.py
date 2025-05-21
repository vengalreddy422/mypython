#Program for List Numerical Values and Find Biggest and smallest among them
# and check for Equality
#AnonymousFunEx5.py
findlistmax=lambda lst: sorted(lst)[-1]
findlistmin=lambda lst: sorted(lst)[0]

#Main Program
print("Enter List of Values Separated Space")
lst=[float(val) for val in input().split()]
bv=findlistmax(lst)
sv=findlistmin(lst)
print("Max({})={}".format(lst,bv))
print("Min({})={}".format(lst,sv))
