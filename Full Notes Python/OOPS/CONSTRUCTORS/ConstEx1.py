#ConstEx1.py
class Student:
    def __init__(self): # Deafult OR Parameter-Less Constructor
        print("I am from Deafult Constructor")
        self.sno=100
        self.sname="Rossum"
        print("\tStudent Number={}".format(self.sno))
        print("\tStudent Name={}".format(self.sname))
        print("------------------------------------")

#Main Program
s1=Student() # Object Creation--Makes the PVM to call Deafult Costructor
s2=Student() # Object Creation--Makes the PVM to call Deafult Costructor
s3=Student() # Object Creation--Makes the PVM to call Deafult Costructor


