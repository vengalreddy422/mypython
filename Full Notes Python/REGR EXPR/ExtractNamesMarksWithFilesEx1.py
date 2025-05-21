#Program for Extracting the Names and Marks  from the file where It contains Student Names and Marks
#ExtractNamesMarksWithFilesEx1.py
import re
try:
	with open("E:\\KVR-PYTHON-6PM\\REGR EXPR\\notes\\stud.data","r") as fp:
		filedata=fp.read()
		NamesList=re.findall(r"[A-Z][a-z]+",filedata)
		MarksList=re.findall(r"\d{2}",filedata)
		print("-"*50)
		print("\tNames\t\tMarks")
		print("-"*50)
		for names,marks in zip(NamesList,MarksList):
			print("\t{}\t\t{}".format(names,marks))
		print("-"*50)
except FileNotFoundError:
	print("File Does not Exist")