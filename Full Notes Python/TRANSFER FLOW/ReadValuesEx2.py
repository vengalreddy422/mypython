#Program for Reading N values and Display n Values
#ReadValuesEx2.py
n=int(input("Enter How Many Names u want:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    lst=[] # Create an empty List
    for i in range(1,n+1):
        val=input("Enter {} Value:".format(i))
        lst.append(val)
    else:
        print("List of Words=",lst)