#Program for Serrching  for all Occurence of the word 'Python' with Indices
#RegExp3.py
import re
gd="Python is an oop lang.Python is also Fun prog lang"
sp="Python"
matdet=re.finditer(sp,gd) # Here an object matdet is an object of <class 'callable_iterator'>
print("--------------------------------------------------")
for mat in matdet: # here mat is an object of <class, re.Match>
	print("Start Index:{}   End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------------")
