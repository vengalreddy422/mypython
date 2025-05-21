#PolyEx14.py
class Circle:
    def __init__(self):#Original Constructor
        print("Constructor--Circle Drawing")
class Rect:
    def __init__(self): # Original Constructor
        print("Constructor--Rect Drawing")
class Square(Rect,Circle):
    def __init__(self): # Overridden Constructor
        print("Constructor--Square Drawing")
        super().__init__() # OR Rect.__init__(self)
        Circle.__init__(self)
#Main Program
print("w.r.t Square Class Object")
s=Square() # Object Creation--Makes the PVM to Call Constructor
