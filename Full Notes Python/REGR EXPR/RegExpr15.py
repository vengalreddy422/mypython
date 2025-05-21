#Program for Searching all Special Symbols
#RegExpr15.py
import re
gd="b UVp5#HLs6KNwc@8aDMxR7Z&"
sp="[^A-Za-z0-9]" # Search Pattern
matdet=re.finditer(sp,gd)
print("--------------------------------------------------")
for mat in matdet:
	print("Start Index:{}   End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------------")

