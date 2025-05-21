#Program for Searching  all values Individually
#RegExpr26.py
import re
gd="KVKKVKKKVKV"
sp="."
matdet=re.finditer(sp,gd)
print("--------------------------------------------------")
for mat in matdet:
	print("Start Index:{}   End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------------")

