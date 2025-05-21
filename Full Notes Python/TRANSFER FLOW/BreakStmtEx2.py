#Program for Demonstrating the Need of break keyword
#BreakStmtEx2.py
s="PYTHON"
print("-----------------------------------------------")
print("By using while loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("else part of for loop")
print("-----------------------------------------------")
#Today : My Req: I want to disp: PYTH Only without using Indexing and Slicing
i=0
while(i<len(s)): # s="PYTHON"
    if(s[i]=="O"):
        break
    print(s[i],end="")
    i+=1
else:
    print("else part of for loop")
print()
print("-----------------------------------------------")
print("I am from Other Statements of the Program")
