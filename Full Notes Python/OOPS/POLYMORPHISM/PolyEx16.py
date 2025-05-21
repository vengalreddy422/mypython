#PolyEx16.py
class Circle:
    def area(self): # Original Method
        self.r=float(input("Enter Radius:"))
        self.ac=3.14*self.r**2
        print("Area of Circle=",self.ac)
class Square:
    def area(self):# Original Method
        self.s = float(input("Enter Side:"))
        self.sa = self.s ** 2
        print("Area of Square=", self.sa)

class Rect(Circle,Square):
    def area(self): # Overridden Method
        self.L = float(input("Enter Length:"))
        self.B = float(input("Enter Breadth:"))
        self.ra = self.L * self.B
        print("Area of Rectangle=", self.ra)
        print("-----------------------------------")
        super().area() # OR Circle.area(self)
        print("-----------------------------------")
        Square.area(self)

#Main Program
r=Rect()
r.area()