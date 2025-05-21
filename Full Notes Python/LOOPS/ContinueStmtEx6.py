#program for accepting a Line of Text and Get Only Vowels
#ContinueStmtEx6.py
line=input("Enter Line of Text:")
nov=0
print("Vowels List")
for ch in line:
    if ch.lower() not in list("aeiou"):
        continue
    print(ch, end=",")
    nov=nov+1
print("\nNumber of Vowels Found=",nov)

