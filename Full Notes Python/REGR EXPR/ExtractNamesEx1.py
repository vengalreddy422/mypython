#Program for Extracting the Names from Given Text
#ExtractNamesEx1.py
import re
gd="Rossum got 55 marks, Travis got 44 marks , Ritche got 66 marks and Jhon got 35 marks and Anthony got 77 marks"
sp="[A-Z][a-z]+"
res=re.findall(sp,gd)
print("------------------------------------")
print("List of Names")
print("------------------------------------")
for word in res:
	print(word)
print("------------------------------------")
	