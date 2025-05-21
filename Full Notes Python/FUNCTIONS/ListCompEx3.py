#ListCompEx3.py
print("Enter List of Values Separated by Comma:")
posvals=[ float(val)    for val in input().split(",")  if float(val)>0 ]
print("Possitive Values=",posvals)