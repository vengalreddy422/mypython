#DictCompEx4.py
print("Enter List of Words Separated by Comma")
wordslength={word:len(word) for word in input().split(",")}
for word,length in wordslength.items():
    print('\t{}---{}'.format(word,length))
