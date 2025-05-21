#SumAvgEx3.py
def getvals():
    nov=int(input("Enter How Many Values u want:"))
    if(nov<=0):
        return [] # returning empty List
    else:
        lst=[]
        for i in range(1,nov+1):
            val=float(input("Enter {} Value:".format(i)))
            lst.append(val)
        return lst

def findsumavg():
    lst=getvals() # Function Call
    if(len(lst)==0):
        print("Empty List--cant find sum and avg")
    else:
        print("Given List={}".format(lst))
        print("Sum={}".format(sum(lst)))
        print("Average={}".format(sum(lst)/len(lst)))

#Main Program
findsumavg() # Function Call