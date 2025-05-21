#PolyEx7.py
class Circle:
    def draw(self): # Original Method
        print("Drawing Circle")
        #super().draw()---Invalid bcoz 'object' class does not contain draw()
    def hello(self):
        print("Hello Circle")
class Square:
    def draw(self): # Original Method
        print("Drawing Square")
    def hello(self):
        print("Hello Square")
class Rect(Square,Circle):
    def draw(self): # Overridden method
        print("Drawing Rect")
        Circle.draw(self)
        Square.draw(self)
    def hello(self):
        print("Hello Rect")
        Circle.hello(self)
        Square.hello(self)

#main program
r=Rect()
r.draw()
print("--------------------------")
r.hello()

