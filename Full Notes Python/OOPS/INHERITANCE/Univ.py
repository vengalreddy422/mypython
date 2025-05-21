#Univ.py<---File Name and Module Name
class Univ:
    def getUnivDet(self):
        self.uname=input("Enter University Name:")
        self.uloc=input("Enter University Location:")
    def dispUnivDet(self):
        print("-" * 50)
        print("University Name:{}".format(self.uname))
        print("University Location:{}".format(self.uloc))
        print("-" * 50)
