#Program for Finding Number of Words and their Length
#NumberOfWordsWithLengthEx1.py
line=input("Enter a Line of Text:")
if(line.isspace()):
    print("Don't enter space for Line of Text:")
elif(len(line)==0):
    print("Line shloud not be empty")
else:
    print("---------------------------------")
    print("Given Line={}".format(line))
    words=line.split()
    print("Number of words=",len(words))
    print("---------------------------------")
    for word in words:
        print("\t{}--->{}".format(word,len(word)))
    print("---------------------------------")