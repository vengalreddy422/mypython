#Program for Extracting the Mail Ids from file where It contains Names an Mails with Other Information
#ExtractNamesMaildsWithFilesEx1.py
import re
try:
	with open("E:\\KVR-PYTHON-6PM\\REGR EXPR\\notes\\mails.data","r") as fp:
		filedata=fp.read()
		NamesList=re.findall(r"[A-Z][a-z]+",filedata)
		MailsList=re.findall(r"\S+@\S+",filedata)
		print("-"*50)
		print("\tNames\t\tMail-Id")
		print("-"*50)
		for names,mail in zip(NamesList,MailsList):
			print("\t{}\t\t{}".format(names,mail))
		print("-"*50)

except FileNotFoundError:
	print("File Does not Exist")
