#icici.py<----File Name and Module Name
bname="ICICI"
addr="AMPT-HYD" # Here bname and addr are called Global Variables
def simpleint(): # Function Def...
    p=float(input("Enter Principle Amount:"))
    t=float(input("Enter Time:"))
    r=float(input("Enter Rate:"))
    #cal si
    si=(p*t*r)/100
    print("-"*50)
    print("\tPrinciple Amount={}".format(p))
    print("\tTime={}".format(t))
    print("\tRate={}".format(r))
    print("\tSimple Interrest={}".format(si))
    print("-" * 50)