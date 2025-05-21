#Program for Demonstrating the Need of break keyword
#BreakStmtEx1.py
s="PYTHON"
print("-----------------------------------------------")
print("By using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("else part of for loop")
print("-----------------------------------------------")
#Today : My Req: I want to disp: PYTH Only without using Indexing and Slicing
for ch in s: # s="PYTHON"
    if(ch=="O"):
        break
    print(ch,end="")
else:
    print("else part of for loop")
print()
print("-----------------------------------------------")
print("I am from Other Statements of the Program")
