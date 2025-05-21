#Program for Saving Dict Data into JSON File
#DictObjectDataToJsonFile.py
import json
DictData={'ENO': 100, 'ENAME': 'Rossum', 'SAL': 4.5, 'DSG': 'Author'}
print("------------------------------------------------------------------------")
print("Dict Data=",DictData)
print("Type of DictData=",type(DictData))
print("------------------------------------------------------------------------")
with open("E:\\KVR-PYTHON-6PM\\JSON\\NOTES\\emp.json","w") as fp:
	json.dump(DictData,fp)
	print("Dict Object Data Saved in Json File--Verify")
print("------------------------------------------------------------------------")

