#DecEx5.py
def toLower(GL):
	def convertintolower():
		line,upc=GL()
		lwc=line.lower()
		return line,upc,lwc
	return convertintolower

def toUpper(GL):
	def convertintoupper():
		line=GL()
		return (line,line.upper())
	return convertintoupper

@toLower
@toUpper
def getLine():
	return input("Enter a Line of Text:")

#main Program
line,upc,lwc=getLine()
print("-"*50)
print("Given Line={}".format(line))
print("Upper Case={}".format(upc))
print("Lower Case={}".format(lwc))
print("-"*50)