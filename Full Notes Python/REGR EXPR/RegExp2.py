#Program for Searching  for first Occurence of the word 'Python'.
#RegExp2.py
import re
gd="Python is an oop lang.Python is also Fun prog lang"
sp="Python"
matdet=re.search(sp,gd) # here matdet object can be either <class, re.match> or <class, NoneType>
if(matdet!=None):
	print("Search is Sucessful")
	print("\tStart Index:{}".format(matdet.start()))
	print("\tEnd Index:{}".format(matdet.end()))
	print("\tValue :{}".format(matdet.group()))
else:
	print("Search is Not Sucessful")
	print("'{}' Does not Exist".format(sp))

