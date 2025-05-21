#Program for Searching Zero K or One K or More Ks
#RegExpr24.py
import re
gd="KVKKVKKKVKV"
sp="K*"
matdet=re.finditer(sp,gd)
print("--------------------------------------------------")
for mat in matdet:
	print("Start Index:{}   End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------------")

