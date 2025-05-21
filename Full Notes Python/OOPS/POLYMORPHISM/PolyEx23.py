#PolyEx23.py
class Circle:
    def __init__(self,r): # Original Constructor
        self.ac=3.14*r**2
        print("Area of Circle=",self.ac)
class Square(Circle):
    def __init__(self,s):# Overridden Constructor
        self.sa = s ** 2
        print("Area of Square=", self.sa)
        print("-----------------------------------")
class Rect(Square):
    def __init__(self,s=0):
        self.area(L,B)
    def area(self,L,B): # Overridden Constructor
        self.ra = L*B
        print("Area of Rectangle=", self.ra)
        print("-----------------------------------")
        Square.__init__(self,float(input("Enter Side:")))
        Circle.__init__(self,float(input("Enter Radius:")))
#Main Program
L=float(input("Enter Length:"))
B=float(input("Enter Breadth:"))
r=Rect() # Object Creation--PVM calls Default Constructor
