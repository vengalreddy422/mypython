#DivisionDemo2.py<---File Name & Main Program
from Division import divop
from DivExcept import ZeroError
try:
    a=float(input("Enter Value a:"))
    b=float(input("Enter Value b:"))
    res=divop(a,b) # Function Call--gives either Result or exception.
except (ZeroError,ValueError):
    print("\tDon't Enter Zero for Den...")
    print("\tDon't Enter alnums,strs and symbols ")
else:
    print("Div=", res)


#Phase-3: Handling the Exceptions.    