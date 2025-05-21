#Program for Accepting a Value from KBD and Decide whether It is Palindrome or not
#TernaryOpEx1.py
val=input("Enter a Value:") # val=LIRIL
res =  "Palindrome" if  val==val[::-1] else  "Not Palindrome"
print("{} is {}".format(val,res))

