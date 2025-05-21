#Program for   Loading / Reading JSON File Data into Dict Object Data .
#JsonFileToDictObject.py
import json
try:
	with open("E:\\KVR-PYTHON-6PM\\JSON\\NOTES\\emp.json","r") as fp:
		DictData=json.load(fp)
		print("Dict Data=",DictData)
		print("Type of DictData=",type(DictData))
		print("------------------------------------------------------------------------")
		for key,value in DictData.items():
			print("\t{}---->{}".format(key,value))
		print("------------------------------------------------------------------------")
except FileNotFoundError:
	print("Json File Does not Exist")