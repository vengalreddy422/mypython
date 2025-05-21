#NameValidationDemo.py
from NameValidationProcess import validate
from NameValidationExcept import SpaceError, ZeroLengthError, InvalidNameError
try:
    name=input("Enter Ur Name:")
    vaidname=validate(name) # Function Call
except SpaceError:
    print("\tDon't Enter Space space for Ur Name:")
except ZeroLengthError:
    print("\tU Must Enter UR name")
except InvalidNameError:
    print("\tUr Name is Invalid")
else:
    print("'{}' is Valid Name".format(name))

