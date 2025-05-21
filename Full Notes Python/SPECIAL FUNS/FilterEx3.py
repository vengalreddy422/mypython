#Program for Filtering +ve Values from List of Values
#FilterEx3.py
print("Enter List of Values  Separated by Space")
lst=[float(val) for val in input().split()]
pslist=tuple(filter(lambda val:val>0,lst)) # here pos is a Anonymous function
print("Given List of Values=",lst)
print("+Ve Values=",pslist)
