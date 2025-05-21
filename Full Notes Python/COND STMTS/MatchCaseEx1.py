#Program for Implementaing all Arithmetic Operations by using match case
#MatchCaseEx1.py
import sys
print("*"*50)
print("\t\tARITHMETIC OPERATIONS")
print("*"*50)
print("\t\t1. Addition")
print("\t\t2. Substraction")
print("\t\t3. Multiplication")
print("\t\t4. Division")
print("\t\t5. Modulo Div")
print("\t\t6. Exponentiation")
print("\t\t7. Exit")
print("*"*50)
ch=int(input("Enter Ur Choice:"))
match(ch):
    case 1 :
        print("Enter Two values for Addition:")
        a,b=float(input()),float(input())
        print("\t\tSum({},{})={}".format(a,b,a+b))
    case 2|20:
        print("Enter Two values for Substraction:")
        a, b = float(input()), float(input())
        print("\t\tSub({},{})={}".format(a, b, a - b))
    case 3:
        print("Enter Two values for Multiplication:")
        a, b = float(input()), float(input())
        print("\t\tMul({},{})={}".format(a, b, a * b))
    case 4:
        print("Enter Two values for Division:")
        a, b = float(input()), float(input())
        print("\t\tDiv({},{})={}".format(a, b, a / b))
        print("\t\tFloorDiv({},{})={}".format(a, b, a // b))
    case 5:
        print("Enter Two values for Modulo Div:")
        a, b = float(input()), float(input())
        print("\t\tMod({},{})={}".format(a, b, a % b))
    case 6:
        a, b = float(input("Enter Base:")), float(input("Enter Power:"))
        print("\t\tPow({},{})={}".format(a, b, a ** b))
    case 7:
        print("Thx for This Program")
        sys.exit() # physical Termination of the Program
    case _: # Default Case Block--to written at last
        print("Ur Selection of Operation is wrong")
print("Program Execution Completed")
