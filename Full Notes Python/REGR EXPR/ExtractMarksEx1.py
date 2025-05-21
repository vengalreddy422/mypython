#Program for Extracting the Marks from Given Text
#ExtractMarksEx1.py
import re
gd="Rossum got 55 marks, Travis got 44 marks , Ritche got 66 marks and Jhon got 35 marks and Anthony got 77 marks"
sp=r"\d{2}"
res=re.findall(sp,gd)
print("------------------------------------")
print("List of Marks")
print("------------------------------------")
for marks in res:
	print(marks)
print("------------------------------------")
	