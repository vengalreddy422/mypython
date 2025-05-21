#Program for Converting JSON String Data into Dict Object---json.loads()
#JsonStrDataToDictData.py
import json
jsonstrdata=' {"ENO":"100","ENAME":"Rossum","SAL":"4.5","DSG":"Author"}'
print("Json Str Data=",jsonstrdata)
print("Type of jsonstrdata=",type(jsonstrdata))
print("------------------------------------------------------------------------")
DictData=json.loads(jsonstrdata)
print("Dict Data=",DictData)
print("Type of DictData=",type(DictData))
print("------------------------------------------------------------------------")
for key,value in DictData.items():
	print("\t{}---->{}".format(key,value))
print("------------------------------------------------------------------------")