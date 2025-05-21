#Program for Filtering Alphabets from Line of Text
#FilterEx4.py
line=input("Enter Line of Text:") # Pyt9hon i#s an oop"
alphabets=list(filter(lambda ch:ch.isalpha(),line))
print("List of Alphabets from Gien Line")
print("".join(alphabets))
