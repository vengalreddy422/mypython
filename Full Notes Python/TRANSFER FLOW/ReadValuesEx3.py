#Program for Reading Number values until we press @
#ReadValuesEx3.py
lst=list()
print("Enter List of Numrical Values (Press @ to Stop)")
while(True):
    value=input()
    if(value=="@"):
        break
    else:
        lst.append(float(value))

print("List of Values=",tuple(lst))


