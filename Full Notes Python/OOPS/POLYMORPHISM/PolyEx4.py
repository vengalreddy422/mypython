#PolyEx4.py
class Circle:
    def draw(self): # Original Method
        print("Drawing Circle")
        #super().draw()---Invalid bcoz 'object' class does not contain draw()
class Square(Circle):
    def draw(self): # Overridden method
        print("Drawing Square")
        super().draw()
class Rect(Square):
    def draw(self): # Overridden method
        print("Drawing Rect")
        super().draw()

#main program
r=Rect()
r.draw()