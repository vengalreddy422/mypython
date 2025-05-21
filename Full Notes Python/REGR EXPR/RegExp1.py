#Program for Saerching the word 'Python'.
#RegExp1.py
import re
gd="Python is an oop lang.Python is also Fun prog lang"
sp="Python"
words=re.findall(sp,gd)
if(len(words)!=0):
	print("Search is Sucessful")
	print("'{}' Found {} Time(s)".format(sp,len(words)))
else:
	print("Search is Un-Sucessful")
	print("'{}' Found {} Time(s)".format(sp,len(words)))
