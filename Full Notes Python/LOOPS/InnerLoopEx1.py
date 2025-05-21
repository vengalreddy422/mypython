#Program for Demonstrating the Need of Inner Loops
#InnerLoopEx1.py
for i in range(1,6): # Outer loop
	print("="*50)
	print("Outer Loop-Value of i=",i)
	print("-----------------------------------------")
	for j in range(1,4): # Inner Loop
		print("\tInner loop-Val of j=",j)
	else:
		print("-----------------------------------------")
		print("Out-off inner loop")
else:
	print("Out-off Outer loop")
	print("="*50)

