#Program for Reading Number values until we press @
#ReadValuesEx3.py
d={}
print("Enter List of Key, Values (Press @ to Stop)")
print("-------------------------------------------------")
while(True):
    key=input("Enter Key:")
    if (key == "@"):
        break
    if(key!='@'):
        value=input("Enter Value:")
    d[key]=value
print("-------------------------------------------------")
for k,v in d.items():
    print("{}-->{}".format(k,v))
print("-------------------------------------------------")

