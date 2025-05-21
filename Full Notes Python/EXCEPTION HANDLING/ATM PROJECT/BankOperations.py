#BankOperations.py<---File Name and Module Name
from ATMExceptions import WithdrawError,InSuffFundError,DepositError
bal=500.00 # here bal is call Global Variable
def deposit():
    damt=float(input("Enter Ur Deposit Amount:")) # there is a possibility of getting ValueError
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tUR Account xxxxxxxx123 Credited with INR:{}".format(damt))
        print("\tNow Available Balance in xxxxxxxx123 INR:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter UR Withdraw Amount:")) # there is a possibility of getting ValueError
    if(wamt<=0):
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("\tUR Account xxxxxxxx123 Debitted with INR:{}".format(wamt))
        print("\tNow Available Balance in xxxxxxxx123 INR:{}".format(bal))
def balenq():
    print("\tAvailable Balance in UR xxxxxxxx123 INR:{}".format(bal))