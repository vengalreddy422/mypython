#Program for Extracting the Words from Given Text
#ExtractWordsEx1.py
import re
gd="Rossum got 55 marks, Travis got 44 marks , Ritche got 66 marks and Jhon got 35 marks and Anthony got 77 marks"
sp="[A-Za-z]+"
res=re.finditer(sp,gd)
for mat in res:
	print(mat.group())