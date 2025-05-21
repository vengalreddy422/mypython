#PolyEx22.py
class Circle:
    def __init__(self,r): # Original Constructor
        self.ac=3.14*r**2
        print("Area of Circle=",self.ac)
class Square:
    def __init__(self,s):# Original Constructor
        self.sa = s ** 2
        print("Area of Square=", self.sa)
        print("-----------------------------------")
class Rect(Circle,Square):
    def __init__(self,L,B): # Overridden Constructor
        self.ra = L*B
        print("Area of Rectangle=", self.ra)
        print("-----------------------------------")
        Square.__init__(self,float(input("Enter Side:")))
        print("-----------------------------------")
        Circle.__init__(self, float(input("Enter Radius:")))


#Main Program
Rect(float(input("Enter Length:")),float(input("Enter Breadth:"))) # Object Creation--PVM calls Constructor
