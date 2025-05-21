#PolyEx17.py
class Circle:
    def area(self,r): # Original Method
        self.ac=3.14*r**2
        print("Area of Circle=",self.ac)
class Square(Circle):
    def area(self,s):# Overridden Method
        self.sa = s ** 2
        print("Area of Square=", self.sa)
        print("-----------------------------------")
        super().area(float(input("Enter Radius Value:")))
class Rect(Square):
    def area(self,L,B): # Overridden Method
        self.ra = L*B
        print("Area of Rectangle=", self.ra)
        print("-----------------------------------")
        super().area(float(input("Enter Side Value:")))

#Main Program
r=Rect()
L = float(input("Enter Length:"))
B = float(input("Enter Breadth:"))
r.area(L,B)