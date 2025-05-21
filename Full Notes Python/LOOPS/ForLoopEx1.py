#Program for accepting a Word and display Its Chars
#ForLoopEx1.py
s=input("Enter a Word:")
print("By using while Loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
print("-----------------------------")
print("By using for Loop")
for ch in s: # s="PYTHON"
    print("\t{}".format(ch))
print("-----------------------------")