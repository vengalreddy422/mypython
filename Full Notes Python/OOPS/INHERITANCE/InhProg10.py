#InhProg8.py
class GrandParent:
    def getGrandParentProp(self):
        self.gpp=float(input("Enter Grand Parent Property:"))
class Parent:
    def getParentProp(self):
        self.pp=float(input("Enter Parent Property:"))
class Child(GrandParent,Parent):
    def getChildProperty(self):
        self.cp=float(input("Enter Child Property:"))
    def getTotalProp(self):
        self.getGrandParentProp()
        self.getParentProp()
        self.getChildProperty()
        self.tp=self.gpp+self.pp+self.cp
        print("Parent Grand Property={}".format(self.gpp))
        print("Parent Property={}".format(self.pp))
        print("Child Property={}".format(self.cp))
        print("Total Property={}".format(self.tp))
#main Program
co=Child()
co.getTotalProp()

