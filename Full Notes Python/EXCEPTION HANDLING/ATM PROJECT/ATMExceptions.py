#ATMExceptions.py<---Main Program
class DepositError(Exception):pass
class WithdrawError(BaseException):pass
class InSuffFundError(Exception):pass