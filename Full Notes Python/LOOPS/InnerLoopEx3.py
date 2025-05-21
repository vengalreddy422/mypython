#Program for Demonstrating the Need of Inner Loops
#InnerLoopEx3.py
i=5
while(i>=1): # Outer loop
	print("="*50)
	print("Outer Loop-Value of i=",i)
	print("-----------------------------------------")
	for j in range(3,0,-1): # Inner Loop
		print("\tInner loop-Val of j=",j)
	else:
		i=i-1
		print("-----------------------------------------")
		print("\tOut-off inner loop")
else:
	print("Out-off Outer loop")
	print("="*50)