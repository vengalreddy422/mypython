#Program for Reading the Values from Keyboard
#ListCompEx2.py
print("Enter List of Values Separated by Comma:")
lst=[float(val) for val in input().split(",")] # s=10 20 30 40 50 60 70
print("Content of List=",lst)
print("Type of Lst=",type(lst))
