#TestQuestionwithDynamic.py
def readwords() :
	lst=[]
	print("Enter List of Words(Press @ to stop):")
	while(True):
		word=input()
		if(word!="@"):
			lst.append(word)
		else:
			break
	return lst

def docapitalize(words):
	cp=[]
	for word in words:
		cp.append(word.capitalize())
	return cp

def doupper(words):
	upc=[]
	for word in words:
		upc.append(word.upper())
	return upc

def dolower(words):
	lwc=[]
	for word in words:
		lwc.append(word.lower())
	return lwc
#main Program
words=readwords() # Function Call
cp=docapitalize(words) # Function call
upc=doupper(words) # Function Call
lwc=dolower(words) # Function Call
print("-----------------------------------------")
print("Given Data=",words)
print("Capitalized Data=",cp)
print("Upper Case Data=",upc)
print("Lower Case Data=",lwc)
print("-----------------------------------------")