#Accept the Salaries range 0 to 1000
#Obtain those Salaries ranges 0 to 500 from given Salaries and
#      give 10% Hike and Find Total Salary Before Hike and after Hike.
#Obtain those Salaries ranges 501 to 1000 from given Salaries and
#      give 5% Hike and Find Total Salary Before Hike and after Hike.
#Find Total Salary before and after Hike.
#FilterMapReduceEx.py
import functools
#Get Salaries ranges from 0 to 1000
print("Enter List of Salaries ranges from 0 to 1000:")
sallist=[float(sal) for sal in input().split() if float(sal) in range(0,1001)]
#Obtain those Salaries ranges 0 to 500 from given Salaries
sal0_500=list(filter(lambda sal: sal in range(0,501),sallist))
#btain those Salaries ranges 501 to 1000 from given Salaries
sal501_1000=list(filter(lambda sal: 501<=sal<=1000,sallist))
#give 10% Hike for 0 to 500
hikesal0_500=list(map(lambda sal:sal+sal*10/100,sal0_500))
#give 5% Hike for 501 to 1000
hikesal501_1000=list(map(lambda sal:sal+sal*5/100,sal501_1000))
#Find Total Salary before and After Hike of range 0 to 500
totsal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2,sal0_500)
tothikesal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2,hikesal0_500)
#Find Total Salary before and After Hike of range 501 to 1000
totsal501_1000=functools.reduce(lambda sal1,sal2:sal1+sal2,sal501_1000)
tothikesal501_1000=functools.reduce(lambda sal1,sal2:sal1+sal2,hikesal501_1000)
print("*"*60)
print("Salary0-500\t\tHike Salary0-500")
print("*"*60)
for osl,nsl in zip(sal0_500,hikesal0_500):
    print("\t{}\t\t\t{}".format(osl,nsl))
print("-"*50)
print("\t{}\t\t\t{}".format(totsal0_500,tothikesal0_500))
print("-"*50)
print("*"*60)
print("Salary501-1000\t\tHike Salary501-1000")
print("*"*60)
for osl,nsl in zip(sal501_1000,hikesal501_1000):
    print("\t{}\t\t\t{}".format(osl,nsl))
print("-"*50)
print("\t{}\t\t\t{}".format(totsal501_1000,tothikesal501_1000))
print("-"*50)
print("*"*60)
grandtotal0_1000=totsal0_500+totsal501_1000
grandhiketotal0_1000=tothikesal0_500+tothikesal501_1000
print("\t{}\t\t\t{}".format(grandtotal0_1000,grandhiketotal0_1000))
print("*"*60)
