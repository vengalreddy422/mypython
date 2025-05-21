#Program for Searching all except 'a' or 'b' or 'c' 
#RegExpr5.py
import re
gd="bUVp5#HLs6KNwc@8aDMxR7Z&"
sp="[^abc]" # Search Pattern
matdet=re.finditer(sp,gd)
print("--------------------------------------------------")
for mat in matdet:
	print("Start Index:{}   End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------------")

