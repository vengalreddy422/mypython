#RectAreaPeri.py
def arearect():
    L=float(input("Enter Length of Rect:"))
    B = float(input("Enter Breadth of Rect:"))
    ar=L*B
    print("------------------------------------")
    print("\tLength={}".format(L))
    print("\tBreadth={}".format(B))
    print("\tArea of Rect={}".format(ar))
    print("------------------------------------")
def perirect():
    L = float(input("Enter Length of Rect:"))
    B = float(input("Enter Breadth of Rect:"))
    pr = 2*(L + B)
    print("------------------------------------")
    print("\tLength={}".format(L))
    print("\tBreadth={}".format(B))
    print("\tPerimeter of Rect={}".format(pr))
    print("------------------------------------")

#Main Program
perirect() # function call
print("-----------------------------")
arearect() # function call