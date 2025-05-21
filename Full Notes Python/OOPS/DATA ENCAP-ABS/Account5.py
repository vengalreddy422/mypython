#Program for Demonstrating Data Encapsulation
#Account5.py<----File Name and Module Name
class __Account:
    def __init__(self): # Constructor can't be hidden
        self.acno=123
        self.cname="Rossum"
        self.bal=4.5
        self.pin=4578
        self.bname="SBI"