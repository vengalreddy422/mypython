#program for Cal Simple Interest and Total amount to pay
#ArithmeticOpEx3.py
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
#cal si and total amount to pay
si=(p*t*r)/100
totamt=p+si
print("*"*50)
print("\t\tResult of Simple Interest")
print("*"*50)
print("\t\tPrinciple Amount:{}".format(p))
print("\t\tTime:{}".format(t))
print("\t\tRate of Interest:{}".format(r))
print("\t\tSimple Interest:{}".format(si))
print("\t\tTotal Amount to pay:{}".format(totamt))
print("*"*50)
