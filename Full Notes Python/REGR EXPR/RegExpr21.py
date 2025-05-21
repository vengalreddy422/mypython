#Program for Searching all  except space Char
#RegExpr21.py
import re
gd="b UVp5# HLs6KNwc@8aDMxR7Z&"
sp=r"\S" # Search Pattern
matdet=re.finditer(sp,gd)
print("--------------------------------------------------")
for mat in matdet:
	print("Start Index:{}   End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------------")

