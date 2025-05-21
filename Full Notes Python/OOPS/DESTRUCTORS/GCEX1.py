#GCEX1.py
import gc
print("----------------------------------------------------------")
print("Program Execution Started")
print("Initially, Is  GC Running?=",gc.isenabled()) # True
print("----------------------------------------------------------")
a=10
b=20
gc.disable()
print("Val of a=",a)
print("Val of b=",b)
print("Now Is  GC Running?=",gc.isenabled()) # False
gc.enable()
c=a+b
print("Program Execution Ended")
print("Now Is  GC Running?=",gc.isenabled()) # True
print("----------------------------------------------------------")
