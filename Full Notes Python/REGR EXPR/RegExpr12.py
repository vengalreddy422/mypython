#Program for Searching all Digits
#RegExpr12.py
import re
gd="bUVp5#HLs6KNwc@8aDMxR7Z&"
sp="[0-9]" # Search Pattern
matdet=re.finditer(sp,gd)
print("--------------------------------------------------")
for mat in matdet:
	print("Start Index:{}   End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------------")

