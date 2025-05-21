#MulTableDemo.py
from MulTable import table
from MulExcept import ZeroError,NegativeNumberError
try:
    n=int(input("Enter a Number for Generating Mul Table:"))
    table(n) # Function Call--either Gives result or exception
except ZeroError:
    print("\tDon't Enter Zero for Mul Table")
except NegativeNumberError:
    print("\tDon't -Ve Number for Mul table")
except ValueError:
    print("\tDon't enter alnums, strs and symbols")
