#Program for Two Lists of Elements and Add them with equal Elements
#MapEx5.py
print("Enter First List Elements:")
lst1=[float(val) for val in input().split()]
print("Enter Second List Elements:")
lst2=[float(val) for val in input().split()]
#add lst1 and lst2 and place them in lst3
lst3=list(map(lambda k,v:k+v , lst1,lst2))
print('-'*60)
print("\tLIST1\tLIST2\t\tLIST3")
print('-'*60)
for x,y,z in zip(lst1,lst2,lst3):
    print("\t{}\t{}\t\t\t{}".format(x,y,z))
print('-'*60)
