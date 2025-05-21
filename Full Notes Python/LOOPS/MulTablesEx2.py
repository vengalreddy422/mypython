#Program for Generating  Mul Tables for Random Numbers
#MulTablesEx2.py
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
#Code for Mul tables
for num in lst:
	if(num<=0):
		print("\t{} is invalid input".format(num))
	else:
		print('-'*50)
		print("\tMul Table:{}".format(num))
		print('-'*50)
		for i in range(1,11):
			print("\t{} x {} = {}".format(num,i,num*i))
		print('-'*50)
