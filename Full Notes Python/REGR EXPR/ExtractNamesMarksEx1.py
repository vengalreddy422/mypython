#Program for Extracting the Names and Marks  from Given Text
#ExtractNamesMarksEx1.py
import re
gd="Rossum got 55 marks, Travis got 44 marks , Ritche got 66 marks and Jhon got 35 marks and Anthony got 77 marks and Kvr got 17 marks"

NamesList=re.findall(r"[A-Z][a-z]+",gd)
MarksList=re.findall(r"\d{2}",gd)
print("-"*50)
print("\tNames\t\tMarks")
print("-"*50)
for names,marks in zip(NamesList,MarksList):
	print("\t{}\t\t{}".format(names,marks))
print("-"*50)