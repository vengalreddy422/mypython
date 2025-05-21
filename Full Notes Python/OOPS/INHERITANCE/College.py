#College.py<---File Name and Module Name
from Univ import Univ
class College(Univ):
    def getCollegeDet(self):
        self.cname=input("Enter College Name:")
        self.cloc = input("Enter College Location:")
    def dispCollegeDet(self):
        print("-"*50)
        print("College Name:{}".format(self.cname))
        print("College Location:{}".format(self.cloc))
        print("-" * 50)
