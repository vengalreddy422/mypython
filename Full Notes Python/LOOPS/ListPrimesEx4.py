#Program for Listing the Primes from given List of Values
#ListPrimesEx4.py
lst=list()
print("Enter List of Numrical Values (Press @ to Stop)")
while(True):
    value=input()
    if(value=="@"):
        break
    else:
        lst.append(int(value))
print("------------------------------------")
print("List of Values=",tuple(lst)) # (12, 3, -4, 5, 11, 9, 0, -4)
print("------------------------------------")
# Get the Primes
prlist=list()
for num in lst: # Outer Loop-Supply Value
    if(num<=1):
        continue
    res=True
    for i in range(2,num):
        if(num%i==0):
            res=False
            break
    if(res):
        prlist.append(num)
print("------------------------------------")
print("Primes List")
print(prlist)
