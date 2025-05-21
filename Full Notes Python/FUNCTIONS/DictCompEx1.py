#DictCompEx1.py
print("Enter List of Values:")
dictobj={float(val):float(val)**2  for val in input().split()}
print("Content of Dict")
for key,val in dictobj.items():
    print("\t{}--->{}".format(key,val))

print("Type of dictobj=",type(dictobj))
