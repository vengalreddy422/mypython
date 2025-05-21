#Program for Filtering +ve Values from List of Values
#FilterEx2.py
pos=lambda val: val>0
#main Program
print("Enter List of Values  Separated by Space")
lst=[float(val) for val in input().split()]
pslist=tuple(filter(pos,lst)) # here pos is a Anonymous function
print("Given List of Values=",lst)
print("+Ve Values=",pslist)
