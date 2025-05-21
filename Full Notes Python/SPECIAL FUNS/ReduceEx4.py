#Program for accepting List of words and get a line of Text by using reduce()
#ReduceEx4.py
import functools
print("Enter List of Values Separated by Comma:")
lst=[val for val in input().split(",")]
line=functools.reduce(lambda a,b: a+" "+b,lst)
print("Line of Text=",line)


