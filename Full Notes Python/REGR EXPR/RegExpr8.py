#Program for Searching all   Lower Case Letters
#RegExpr8.py
import re
gd="bUVp5#HLs6KNwc@8aDMxR7Z&"
sp="[a-z]" # Search Pattern
matdet=re.finditer(sp,gd)
print("--------------------------------------------------")
for mat in matdet:
	print("Start Index:{}   End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------------")

