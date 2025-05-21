#Program for Performing Any Arithmetic Operation
# based on Arithmetic Op with Two values by using Static Methods
class Arithmetic:
    def getValues(self):
        while(True):
            try:
                self.a=float(input("Enter First Value:"))
                self.b = float(input("Enter Second Value:"))
                self.op=input("Enter Any Arithmetic Operator:")
            except ValueError:
                print("Don't enter alnums,strs and symbols--try again")
            else:
                break
class Calculator:
    @staticmethod
    def operation(ap):
        match(ap.__dict__.get('op')):
            case "+":
                print("Sum({},{})={}".format(ap.__dict__['a'],
                                             ap.__dict__['b'],ap.__dict__['a']+ap.__dict__['b']))
            case "-":
                print("Sub({},{})={}".format(ap.__dict__.get('a'),
                                     ap.__dict__.get('b'), ap.__dict__.get('a') - ap.__dict__.get('b')))
            case "*":
                print("Mul({},{})={}".format(ap.__dict__.get('a'),
                                             ap.__dict__.get('b'), ap.__dict__.get('a') * ap.__dict__.get('b')))
            case "/":
                print("Div({},{})={}".format(ap.__dict__.get('a'),
                                             ap.__dict__.get('b'), ap.__dict__.get('a') / ap.__dict__.get('b')))
            case "//":
                print("FloorDiv({},{})={}".format(ap.__dict__.get('a'),
                                             ap.__dict__.get('b'), ap.__dict__.get('a') // ap.__dict__.get('b')))
            case "%":
                print("ModDiv({},{})={}".format(ap.__dict__.get('a'),
                                             ap.__dict__.get('b'), ap.__dict__.get('a') % ap.__dict__.get('b')))
            case "**":
                print("Pow({},{})={}".format(ap.__dict__.get('a'),
                                             ap.__dict__.get('b'), ap.__dict__.get('a') ** ap.__dict__.get('b')))
            case _:
                print("{} is Invalid Arithmetic Operator".format(ap.__dict__.get('op')))
#main Program
ao=Arithmetic()
ao.getValues()
Calculator.operation(ao)