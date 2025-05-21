#Program for accepting List of Values and find max and min by using reduce()
#ReduceEx3.py
import functools
print("Enter List of Values Separated by Space:")
lst=[float(val) for val in input().split()] # lst=[10,20,15,30,25,40,35]
maxv=functools.reduce(lambda x,y:max(x,y),lst)
print("Max({})={}".format(lst,maxv))
#              OR
maxv=functools.reduce(lambda x,y:x if x>y else y,lst)
print("Max({})={}".format(lst,maxv))
print("========================================")
minv=functools.reduce(lambda x,y:min(x,y),lst)
print("Min({})={}".format(lst,minv))
#              OR
minv=functools.reduce(lambda x,y:x if x<y else y,lst)
print("Min({})={}".format(lst,minv))
