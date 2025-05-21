#DictCompEx6.py
def getwordslengths():
    print("Enter List of Words Separated by Comma")
    wordslength={word:len(word) for word in input().split(",")}
    return wordslength

def findmaxlengthword(wordswithlength):
    print("Max Length Word(s)")
    #Get Max Length Values from Dict Values
    maxlen=max(wordswithlength.values())
    for word,wl in wordswithlength.items():
        if(wl==maxlen):
            print(word)

#Main Program
wordswithlength=getwordslengths()
findmaxlengthword(wordswithlength)
