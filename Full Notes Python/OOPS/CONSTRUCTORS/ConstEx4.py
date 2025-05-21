#ConstEx4.py
class Test:
    def __init__(self,k,v):
        print("I am from Parameterized Constructor")
        self.a=k
        self.b=v
        print("\tValue of a={}".format(self.a))
        print("\tValue of b={}".format(self.b))
        print("------------------------------------")

#Main Program
t1=Test(100,200)#Object Creation--makes the PVM to Call Parameterized Constructor
t2=Test(10,20)#Object Creation--makes the PVM to Call Parameterized Constructor
t3=Test(1000,2000)#Object Creation--makes the PVM to Call Parameterized Constructor