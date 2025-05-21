#Employee.py<----File Name and Module Name
class Employee:
    def __init__(self,eno,name,sal):
        self.eno=eno
        self.name=name
        self.sal=sal
    def dispempvals(self):
        print("\t{}\t\t{}\t\t{}".format(self.eno,self.name,self.sal))


