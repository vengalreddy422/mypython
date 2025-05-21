#Program for deciding whether the Word is Vowel OR Not
#BreakStmtEx7.py
word=input("Enter any Word:") # Orange
res="NOT VOWEL WORD"
for ch in word:
    if(ch.lower() in list("aeiou")):
        res="VOWEL WORD"
        break
print("{} is {}".format(word,res))
