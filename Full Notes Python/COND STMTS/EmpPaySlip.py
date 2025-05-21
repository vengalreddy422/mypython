#EmpPaySlip.py
print("-"*50)
empno=int(input("Enter Employee Number:"))
empname=input("Enter Employee Name:")
empbasicsal=float(input("Enter Employee Basic Salary:"))
print("-"*50)
if(empbasicsal<=0):
    print("Invalid Salary --try again")
else:
    if(empbasicsal>=10000):
        da = (20/100)*empbasicsal
        ta = (10/100)*empbasicsal
        hra = (8/100)*empbasicsal
        ma = (2/100)*empbasicsal
        lic=(2/100)*empbasicsal
        gpf=(1.5/100)*empbasicsal
    elif(empbasicsal<10000):
        da = (10 / 100) * empbasicsal
        ta = (7.5/ 100) * empbasicsal
        hra = (4.5 / 100) * empbasicsal
        ma = (1.5 / 100) * empbasicsal
        lic = (1.5 / 100) * empbasicsal
        gpf = (1.5 / 100) * empbasicsal
    NetSal = (empbasicsal + da + ta + hra + ma) - (lic + gpf)
    #Display pay slip
    print("*"*50)
    print("\tEMPLOYEE PAY SLIP")
    print("*" * 50)
    print("\tEmployee Number:{}".format(empno))
    print("\tEmployee Name:{}".format(empname))
    print("\tEmployee Basic Salary:{}".format(empbasicsal))
    print("\tDA:{}".format(da))
    print("\tTA:{}".format(ta))
    print("\tHRA:{}".format(hra))
    print("\tMA:{}".format(ma))
    print("Deduction")
    print("\tLIC:{}".format(lic))
    print("\tGPF:{}".format(gpf))
    print("*"*50)
    print("\tNet Salary={}".format(NetSal))
    print("*" * 50)

