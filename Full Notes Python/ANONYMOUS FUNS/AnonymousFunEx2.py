#Program for accepting a word OR Value and decide whether It is Palindrome or Not
#AnonymousFunEx2.py
ispalindrome=lambda val: "Palindrome" if val==val[::-1] else "Not Palindrome"
#Main Program
value=input("Enter a Word OR Value:")
res=ispalindrome(value)
print("{} is {}".format(value,res))