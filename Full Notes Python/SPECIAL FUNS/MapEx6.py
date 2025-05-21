#Program for Two Lists of Elements and Add them with Un-equal Elements
#MapEx6.py
print("Enter First List Elements:")
lst1=[float(val) for val in input().split()]
print("Enter Second List Elements:")
lst2=[float(val) for val in input().split()]
if(len(lst1)>len(lst2)):
    for i in range(len(lst1)-len(lst2)):
        lst2.append(0)
elif(len(lst2)>len(lst1)):
    for i in range(len(lst2)-len(lst1)):
        lst1.append(0)
#Add the List Elements
lst3=tuple(map(lambda k,v:k+v, lst1,lst2))
#Display the Result
print('-'*60)
print("\tLIST1\tLIST2\t\tLIST3")
print('-'*60)
for x,y,z in zip(lst1,lst2,lst3):
    print("\t{}\t{}\t\t\t{}".format(x,y,z))
print('-'*60)
