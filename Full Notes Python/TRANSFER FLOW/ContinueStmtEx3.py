#Program for demonstrating the need of continue statement
#ContinueStmtEx3.py
s="PYTHON"
print("By using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("i am from else-part of for loop")
print("---------------------------------------------")
#My Req:  to display PYHN  without using Indexing and Slicing
print("By using for loop")
for ch in s:
    if(ch=="T") or (ch=="O"):
        continue
    print("{}".format(ch),end="")
else:
    print("\ni am from else-part of for loop")
print("---------------------------------------------")