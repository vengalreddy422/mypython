#PolyEx11.py
class Circle:
    def __init__(self):#Original Constructor
        print("Constructor--Circle Drawing")
class Rect(Circle):
    def __init__(self): # Overridden Constructor
        print("Constructor--Rect Drawing")
        super().__init__() # will call Base Class Constructor from Derived Class Constructor

#Main Program
print("w.r.t Rect Class Object")
r=Rect() # Object Creation--Makes the PVM to Call Constructor
