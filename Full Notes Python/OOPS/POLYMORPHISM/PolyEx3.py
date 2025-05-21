#Program for Demonstrating the Polymorphism
#PolyEx3.py
class RS:
    def advises(self):#Original Method
        print("RS Said to all Student--wake-up at 4:30am and Read Notes")

class Stud1(RS):
    def advises(self):#Overridden Method
        print("Stud1 Said to RS--wake-up at 5:00am and Read Notes")

class Stud2(Stud1):
    def advises(self):#Overridden Method
        print("Stud2 Said to RS--wake-up at 8:00am and Read Notes")
        RS.advises(self)# will call base class Original Method from Derived Class Overridden Method
        Stud1.advises(self)

#Main Program
print('w.r.t Stud2')
s2=Stud2()
s2.advises()