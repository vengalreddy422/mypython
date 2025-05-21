#DictCompEx3.py
wds=[wkn for wkn in input("Enter Week Names separated Comma:").split(",")]
wkn={i+1:wds[i] for i in range(0,len(wds))}
print(wkn)