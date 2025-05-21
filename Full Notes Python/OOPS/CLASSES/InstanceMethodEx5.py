#Program for Reading Two values from KBD and Find their sum
# by Using Classes and Objects with Instance Methods
#InstanceMethodEx5.py
class Sum:
    def readvals(self):
        self.a=float(input("Enter First Value:"))
        self.b = float(input("Enter Second Value:"))
    def addvals(self):
        self.c=self.a+self.b
    def dispvals(self):
        print("Val of a={}".format(self.a))
        print("Val of b={}".format(self.b))
        print("Sum={}".format(self.c))
#Main Program
s=Sum() # Object Creation
s.readvals()
s.addvals()
s.dispvals()

