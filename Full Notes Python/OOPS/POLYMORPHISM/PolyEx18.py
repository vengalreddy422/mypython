#PolyEx18.py
class Circle:
    def area(self,r): # Original Method
        self.ac=3.14*r**2
        print("Area of Circle=",self.ac)
class Square:
    def area(self,s):# Original Method
        self.sa = s ** 2
        print("Area of Square=", self.sa)
        print("-----------------------------------")
class Rect(Circle,Square):
    def area(self,L,B): # Overridden Method
        self.ra = L*B
        print("Area of Rectangle=", self.ra)
        print("-----------------------------------")
        Square.area(self,float(input("Enter Side Value:")))
        print("-----------------------------------")
        Circle.area(self, float(input("Enter Radius:")))
#Main Program
r=Rect()
L = float(input("Enter Length:"))
B = float(input("Enter Breadth:"))
r.area(L,B)