#Program for Reading the Values from Keyboard
#TupleCompEx1.py
print("Enter List of Values:")
x=(float(val) for val in input().split()) # s=10 20 30 40 50 60 70
print("Type of x=",type(x)) # here x is of type  <class 'generator'>
#Convert generator object into tuple
tpl=tuple(x)
print("Content of tuple=",tpl)
print("Type of tpl=",type(tpl))
