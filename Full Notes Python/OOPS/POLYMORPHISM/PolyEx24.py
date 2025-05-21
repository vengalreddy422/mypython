#PolyEx24.py
class C1:
    def x(self):
        print("C1-X()")
class C2(C1):
    def x(self):
        print("C2-X()")
class C3(C1):
    def x(self):
        print("C3-X()")
class C4(C2):
    def x(self):
        print("C4-X()")
class C5(C3):
    def x(self):
        print("C5-X()")
class C6(C4,C5):
    def x(self):
        print("C6-X()")
        C1.x(self)
        C2.x(self)
        C3.x(self)
        super().x()  # OR C4.x(self)
        C5.x(self)

#main Program
C6().x() # Name-Less object