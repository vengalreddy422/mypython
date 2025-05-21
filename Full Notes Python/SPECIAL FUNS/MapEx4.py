#Program for aceepting List of Salaries and give 50% Hike to Every Employee
#MapEx4.py
print("Enter List Salaries:")
oldsal=[float(sal) for sal in input().split() if float(sal)>0]
newsal=list(map(lambda sal:sal+sal*50/100,oldsal))
print('-'*60)
print("\tOLD SALARIES\tNEW SALARIES")
print('-'*60)
for old,new in zip(oldsal,newsal):
    print("\t{}\t\t\t{}".format(old,new))
print('-'*60)

