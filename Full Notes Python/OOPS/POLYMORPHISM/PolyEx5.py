#PolyEx5.py
class Circle:
    def draw(self): # Original Method
        print("Drawing Circle")
        #super().draw()---Invalid bcoz 'object' class does not contain draw()
class Square:
    def draw(self): # Original Method
        print("Drawing Square")
class Rect(Square,Circle):
    def draw(self): # Overridden method
        print("Drawing Rect")
        super().draw()
        Circle.draw(self)


#main program
r=Rect()
r.draw()
