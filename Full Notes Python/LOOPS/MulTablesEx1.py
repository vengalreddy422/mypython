#Program for Generating 1 to N Mul Tables where N is +Ve
#MulTablesEx1.py
nt=int(input("Enter How Many Mu Tables u want:"))
if(nt<=0):
	print("\t{} is Invalid input".format(nt))
else:
		for num in range(1,nt+1):
			print('-'*50)
			print("\tMul Table:{}".format(num))
			print('-'*50)
			for i in range(1,11):
				print("\t{} x {} = {}".format(num,i,num*i))
			print('-'*50)