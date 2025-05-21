#Program for Converting Dict Object Data into JSON Str Data
#DictObjectToJsonData.py
DictData={'ENO': 100, 'ENAME': 'Rossum', 'SAL': 4.5, 'DSG': 'Author'}
print("------------------------------------------------------------------------")
print("Dict Data=",DictData)
print("Type of DictData=",type(DictData))
print("------------------------------------------------------------------------")
jsonstrdata=str(DictData)
print("Json Str Data=",jsonstrdata)
print("Type of jsonstrdata=",type(jsonstrdata))
print("------------------------------------------------------------------------")