#Program for demonstrating the need of continue statement
#ContinueStmtEx2.py
s="PYTHON"
print("By using while loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i+=1
else:
    print("i am from else-part of while loop")
print("---------------------------------------------")
#My Req:  to display PYHON without using Indexing and Slicing
print("By using while loop")
i=0
while(i<len(s)):
    if(s[i]=="T"):
        i = i + 1
        continue
    else:
        print("{}".format(s[i]),end="")
        i+=1
else:
    print("\ni am from else-part of while loop")
print("---------------------------------------------")