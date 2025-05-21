#ListCompEx4.py
m=3
n=3
lst=[(i,j) for i in range(m)  for j in range(n)]
for x in lst:
    print(x)
print("--------------------------------------------")
m=2
n=2
lst=[[i,j] for i in range(m)  for j in range(n)]
for x in lst:
    print(x)

print("--------------------------------------------")
