#Program for Reading Two values from KBD and Find their sum
# by Using Classes and Objects with Instance Methods
#InstanceMethodEx6.py
class Sum:
    def readvals(self):
        self.a=float(input("Enter First Value:"))
        self.b = float(input("Enter Second Value:"))
    def addvals(self):
        self.c=self.a+self.b
    def dispvals(self):
        self.readvals()
        self.addvals() # One Instance Method calling another method of same class by using self
        print("Val of a={}".format(self.a))
        print("Val of b={}".format(self.b))
        print("Sum={}".format(self.c))
#Main Program
s=Sum() # Object Creation
s.dispvals()

