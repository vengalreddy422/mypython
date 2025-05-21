#Program for Demonstrating the Need of Inner Loops
#InnerLoopEx2.py
i=1
while(i<=5): # Outer loop
	print("="*50)
	print("Outer Loop-Value of i=",i)
	print("-----------------------------------------")
	j=1
	while(j<=3): # Inner Loop
		print("\tInner loop-Val of j=",j)
		j=j+1
	else:
		i=i+1
		print("-----------------------------------------")
		print("\tOut-off inner loop")
else:
	print("Out-off Outer loop")
	print("="*50)