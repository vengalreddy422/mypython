#Program for Demonstrating the Need of Inner Loops
#InnerLoopEx4.py
for i in range(1,6): # Outer loop
	print("="*50)
	print("Outer Loop-Value of i=",i)
	print("-----------------------------------------")
	j=1
	while(j<=3): # Inner Loop
		print("\tInner loop-Val of j=",j)
		j=j+1
	else:
		print("-----------------------------------------")
		print("\tOut-off inner loop")
else:
	print("Out-off Outer loop")
	print("="*50)