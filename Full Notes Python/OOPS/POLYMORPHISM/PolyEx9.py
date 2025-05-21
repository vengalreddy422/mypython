#PolyEx9.py
class Univ:
    def getDet(self):
        self.uname=input("Enter University Name:")
        self.uloc=input("Enter University Location:")
    def dispDet(self):
        print("-" * 50)
        print("University Name:{}".format(self.uname))
        print("University Location:{}".format(self.uloc))
        print("-" * 50)
class College(Univ):
    def getDet(self):
        self.cname=input("Enter College Name:")
        self.cloc = input("Enter College Location:")
        print("----------------------------------")
        super().getDet()
    def dispDet(self):
        super().dispDet()
        print("-"*50)
        print("College Name:{}".format(self.cname))
        print("College Location:{}".format(self.cloc))
        print("-" * 50)
class Student(College):
    def getDet(self):
        self.sno=int(input("Enter Student Number:"))
        self.name=input("Enter Student Name:")
        self.crs=input("Enter Student Course:")
        print("----------------------------------")
        super().getDet()
        self.dispDet()
    def dispDet(self):
        super().dispDet()
        print("-" * 50)
        print("Student Number:{}".format(self.sno))
        print("Student Name:{}".format(self.name))
        print("Student Course:{}".format(self.crs))
        print("-" * 50)

#main Program
so=Student()
so.getDet()
