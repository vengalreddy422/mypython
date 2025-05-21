#ConstEx2.py
class Student:
    def __init__(self,sno,name): # Parametrized Constructor
        print("I am from Parametrized Constructor")
        self.sno=sno
        self.sname=name
        print("\tStudent Number={}".format(self.sno))
        print("\tStudent Name={}".format(self.sname))
        print("------------------------------------")

#Main Program
s1=Student(100,"Rossum") # Object Creation--Makes the PVM to call Parametrized Costructor
s2=Student(200,"Travis") # Object Creation--Makes the PVM to call Parametrized Costructor
s3=Student(300,"Dennis") # Object Creation--Makes the PVM to call Parametrized Costructor


