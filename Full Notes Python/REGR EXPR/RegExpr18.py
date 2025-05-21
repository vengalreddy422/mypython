#Program for Searching all word Chars(Alphabets +Digits)
#RegExpr18.py
import re
gd="b UVp5#HLs6KNwc@8aDMxR7Z&"
sp=r"\w" # Search Pattern
matdet=re.finditer(sp,gd)
print("--------------------------------------------------")
for mat in matdet:
	print("Start Index:{}   End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------------")

