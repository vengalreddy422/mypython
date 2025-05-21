#Program for Deciding weather the Given Value is Palindrome or not
#SimpleInStmtEx2.py
value=input("Enter a Value:").lower() # PYTHON
if(value==value[::-1]):
    print("{} is Palindrome".format(value))
if(value!=value[::-1]):
    print("{} is Not Palindrome".format(value))
