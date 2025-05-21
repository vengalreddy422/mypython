#Program for accepting a line of Text and Swap Its case without str functions
#ProgSwapCase.py
line=input("Enter a Line of Text:") # line=PYThon
rs=""
for ch in line:
    if ord(ch) in range(65,91):
        rs=rs+chr(ord(ch)+32)
    elif(ord(ch) in range(97,123)):
        rs=rs+chr(ord(ch)-32)
    else:
        rs=rs+chr(ord(ch))
else:
    print("---------------------------------")
    print("Given Line=",line)
    print("Swaped Case Line=",rs)
    print("---------------------------------")