#FunTest.py
#welcome("Rossum")------Gives NameError bcoz Function calls must be after Function Def.
def welcome(name): # Function Def
    print("\tHi {}, Welcome to functions".format(name))

#main Program
print("----------------------------------")
print("Line-6: I am after Function Def")
print("Type of welcome=",type(welcome))
print("----------------------------------")
welcome("Rossum") # Function Call
welcome("Travis") # Function Call