#Program for Finding Number of Words and their Length
#NumberOfWordsWithLengthEx2.py
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
    wd={} # create an empty dict
    for word in words:
        wd[word]=len(word)
    print("---------------------------------")
    for w,wl in wd.items():
        print("\t{}---->{}".format(w,wl))
    print("---------------------------------")