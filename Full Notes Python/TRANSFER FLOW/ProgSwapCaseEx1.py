#Program for accepting a line of Text and Swap Its case
#ProgSwapCase.py
line=input("Enter a Line of Text:") # line=PyThOn
rs=""
for ch in line:
    if ch.isupper():
        rs=rs+ch.lower()
    elif(ch.islower()):
        rs=rs+ch.upper()
    else:
        rs=rs+ch
else:
    print("---------------------------------")
    print("Given Line=",line)
    print("Swaped Case Line=",rs)
    print("---------------------------------")