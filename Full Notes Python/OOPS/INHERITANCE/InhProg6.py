#InhProg6.py
class C1:
    def disp1(self):
        print("C1--disp1()")
class C2(C1):
    def disp2(self):
        print("C2--disp2()")
class C3(C1):
    def disp3(self):
        print("C3--disp3()")
class C4(C2,C3):
    def disp4(self):
        self.disp1()
        self.disp2()
        self.disp3()# Derived Class Method Calling Base Class Method
        print("C4--disp4()")

#Main Program
o4=C4()
o4.disp4()