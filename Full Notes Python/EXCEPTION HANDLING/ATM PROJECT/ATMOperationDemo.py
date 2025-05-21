#ATMOperationDemo.py<---Main Program
from ATMMenu import menu
from ATMExceptions import DepositError,WithdrawError,InSuffFundError
from BankOperations import deposit,withdraw,balenq
while(True):
    menu()
    try:
        ch=int(input("Enter UR Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDon't try to Deposit -VE / Zero Amount")
                except ValueError:
                    print("\tDon't try to Deposit Alnums,strs and symbols")
            case 2:
                try:
                    withdraw()
                except WithdrawError:
                    print("\tDon't try to withdraw -VE / Zero Amount")
                except InSuffFundError:
                    print("\tUR Account does not have Suff Funds--Read Python Notes")
                except ValueError:
                    print("\tDon't try to Withdraw Alnums,strs and symbols")
            case 3:
                balenq()
            case 4:
                print("Thx for this Application")
                break
            case _:
                print("UR Selection of Operation is Wrong-try again")
    except ValueError:
        print("\tDon't Enter Alnums,strs and symbols for Choice--try again")