#InhProg3.py
class C1:
    def disp1(self):
        print("C1--disp1()")
class C2(C1):
    def disp2(self):
        print("C2--disp2()")
class C3(C1):
    def disp3(self):
        print("C3--disp3()")
#Main Program
print("w.r.t C2 Class")
o2=C2()
o2.disp1()
o2.disp2()
print("w.r.t C3 Class")
o3=C3()
o3.disp1()
o3.disp3()


