#Program for Swapping of Any Two Integer Values
#AssignmentOpEx5.py--Logic-4
a,b=int(input("Enter First Value:")),int(input("Enter Second Value:"))
print("-"*50)
print("Original Value of a={}".format(a))
print("Original Value of b={}".format(b))
print("-"*50)
#swapping Logic by without using Third Var
a=a*b
b=a//b
a=a//b
print("Swapped Value of a={}".format(a))
print("Swapped Value of b={}".format(b))
print("-"*50)
