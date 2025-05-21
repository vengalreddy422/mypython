#PolyEx21.py
class Circle:
    def __init__(self,r): # Original Constructor
        self.ac=3.14*r**2
        print("Area of Circle=",self.ac)
class Square(Circle):
    def __init__(self,s):# Overridden Constructor
        self.sa = s ** 2
        print("Area of Square=", self.sa)
        print("-----------------------------------")
        super().__init__(float(input("Enter Radius:")))
class Rect(Square):
    def __init__(self,L,B): # Overridden Constructor
        self.ra = L*B
        print("Area of Rectangle=", self.ra)
        print("-----------------------------------")
        super().__init__(float(input("Enter Side:")))

#Main Program
L = float(input("Enter Length:"))
B = float(input("Enter Breadth:"))
r=Rect(L,B) # Object Creation--PVM calls Constructor
