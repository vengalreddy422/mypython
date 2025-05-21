#MaxMinElementsEx3.py
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
def findmax(lst): # lst=[3.0, 8.0, 1.2, 14.5, 7.88]
    if(len(lst)==0):
        print("List is empty-can't find max value")
    else:
        print("Given List=",lst)
        print("Max Element=",max(lst))
        print("--------OR--------------")
        print("Max Element=", sorted(lst)[-1])
def findmin(lst):
    if(len(lst)==0):
        print("List is empty-can't find min value")
    else:
        print("Given List=", lst)
        print("Min Element=", min(lst))
        print("--------OR--------------")
        print("Min Element=", sorted(lst)[0])

#Main Program
lst=getvals()
findmax(lst) # Function Call
findmin(lst) # Function Call