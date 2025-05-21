#Program for Deciding weather the Given Value is Palindrome or not
#IfElseStmtEx1.py
value=input("Enter a Value:").lower() # LIRIL
if(value==value[::-1]):
    print("{} is Palindrome".format(value))
else:
    print("{} is Not Palindrome".format(value))
print("Program Execution Completed")