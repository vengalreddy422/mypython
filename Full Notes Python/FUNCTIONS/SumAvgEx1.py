#SumAvgEx1.py
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

def findsumavg(lst):
    if(len(lst)==0):
        print("Empty List--cant find sum and avg")
    else:
        s=0
        for val in lst:
            s=s+val
        else:
            print("Given List={}".format(lst))
            print("Sum={}".format(s))
            print("Average={}".format(s/len(lst)))

#Main Program
lst=getvals() # Function Call
findsumavg(lst) # Function Call