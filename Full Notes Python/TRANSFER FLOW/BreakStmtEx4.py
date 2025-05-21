#Program for Demonstrating the Need of break keyword
#BreakStmtEx4.py
s="MISSISSIPPI"
print("-----------------------------------------------")
print("By using while loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("else part of for loop")
print("-----------------------------------------------")
#Today : My Req: I want to disp: MISS Only without using Indexing and Slicing
print("By using while loop")
ctr=0
i=0
while(i<len(s)): # s="MISSISSIPPI"
    if(s[i]=="I"):
        ctr=ctr+1
        if(ctr==2):
            break
    print("{}".format(s[i]),end="")
    i=i+1
else:
    print("else part of for loop")
print("\n-----------------------------------------------")

