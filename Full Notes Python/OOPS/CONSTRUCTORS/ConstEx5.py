#ConstEx5.py
class Test:
    def __init__(self,k=1,v=2):
        print("I am from Default/Parameterized Constructor")
        self.a=k
        self.b=v
        print("\tValue of a={}".format(self.a))
        print("\tValue of b={}".format(self.b))
        print("------------------------------------")
#main Program
t1=Test() #Object Creation--makes the PVM to Call Default Constructor
t2=Test(10,20)#Object Creation--makes the PVM to Call Parameterized Constructor
t3=Test(100)#Object Creation--makes the PVM to Call Parameterized Constructor
t4=Test(v=1000)#Object Creation--makes the PVM to Call Parameterized Constructor
t5=Test(v=30,k=20)#Object Creation--makes the PVM to Call Parameterized Constructor