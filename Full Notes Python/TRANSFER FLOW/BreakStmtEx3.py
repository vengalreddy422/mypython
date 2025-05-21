#Program for Demonstrating the Need of break keyword
#BreakStmtEx3.py
s="MISSISSIPPI"
print("-----------------------------------------------")
print("By using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("else part of for loop")
print("-----------------------------------------------")
#Today : My Req: I want to disp: MISS Only without using Indexing and Slicing
print("By using for loop")
ctr=0
for ch in s: # s="MISSISSIPPI"
    if(ch=="I"):
        ctr=ctr+1
        if(ctr==2):
            break
    print("{}".format(ch),end="")
else:
    print("else part of for loop")
print("\n-----------------------------------------------")
