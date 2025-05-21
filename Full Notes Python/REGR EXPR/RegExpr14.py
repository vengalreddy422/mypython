#Program for Searching all  Alpha-numerics (Aphabets+Digits) Only
#RegExpr14.py
import re
gd="bUVp5#HLs6KNwc@8aDMxR7Z&"
sp="[A-Za-z0-9]" # Search Pattern
matdet=re.finditer(sp,gd)
print("--------------------------------------------------")
for mat in matdet:
	print("Start Index:{}   End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------------")

