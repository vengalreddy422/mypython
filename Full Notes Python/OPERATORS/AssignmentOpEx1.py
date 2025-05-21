#Program for Peforming all Arithmetic Operations by using Multi Line assignment Op
#AssignmentOpEx1.py
a,b=float(input("Enter First Value:")),float(input("Enter Second Value:")) # Multi Line assignment
addop,subop,mulop,divop,fdivop,modop,powop=a+b,a-b,a*b,a/b,a//b,a%b,a**b # Multi Line assignment
print("*"*50)
print("\t\tResults of Arithmertic Operators")
print("*"*50)
print("\t\tSum({},{})={}".format(a,b,addop))
print("\t\tSub({},{})={}".format(a,b,subop))
print("\t\tMul({},{})={}".format(a,b,mulop))
print("\t\tDiv({},{})={}".format(a,b,divop))
print("\t\tFloorDiv({},{})={}".format(a,b,fdivop))
print("\t\tMod({},{})={}".format(a,b,modop))
print("\t\tPow({},{})={}".format(a,b,powop))
print("*"*50)