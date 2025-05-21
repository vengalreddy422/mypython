#Program for Demonstrating the Polymorphism
#PolyEx1.py
class RS:
    def advises(self):#Original Method
        print("RS Said to all Student--wake-up at 4:30am and Read Notes")
class Stud1(RS):
    def advises(self):#Overridden Method
        print("Stud1 Said to RS--wake-up at 5:00am and Read Notes")
        super().advises() # will call base class Original Method from Derived Class Overridden Method

#Main Program
print('w.r.t Stud1')
s1=Stud1()
s1.advises()