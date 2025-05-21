#Program for Reading the Values from Keyboard
#SetCompEx1.py
print("Enter List of Values Separated by Comma:")
st1={float(val) for val in input().split(",")} # s=10 20 30 40 50 60 70
print("Content of Set=",st1)
print("Type of st1=",type(st1))
