#Program for accepting List of Values and find their sum by using reduce()
#ReduceEx1.py
import functools
def sumop(k,v):
    return (k+v)

#Main Program
print("Enter List of Values Separated by Space:")
lst=[float(val) for val in input().split()]
res=functools.reduce(sumop,lst)
print("Sum({})={}".format(lst,res))