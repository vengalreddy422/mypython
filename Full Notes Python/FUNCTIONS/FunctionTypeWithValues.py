#FunctionTypeWithValues.py--Most Imp
def disp(a):
    if(type(a)==int):
        print(a,type(a))
    elif(type(a)==float):
        print(a,type(a))
    elif(type(a)==bool):
        print(a,type(a))
    elif(type(a)==complex):
        print(a,type(a))
        print("\tReal part=",a.real)
        print("\tImag Part=",a.imag)
    elif(type(a)==str):
        print(a,type(a))
        print("Upper Value=",a.upper())
    elif (type(a) == bytes):
        print(a, type(a))
    elif (type(a) == bytearray):
        print(a, type(a))
    elif (type(a) == range):
        print(a, type(a))
        for val in a:
            print("\t{}".format(val))
    elif (type(a) == list):
        print(a, type(a))
        for val in a:
            print("\t{}".format(val))
    elif (type(a) == tuple):
        print(a, type(a))
        for val in a:
            print("\t{}".format(val))
    elif (type(a) == set):
        print(a, type(a))
        for val in a:
            print("\t{}".format(val))
    elif (type(a) == frozenset):
        print(a, type(a))
        for val in a:
            print("\t{}".format(val))
    elif (type(a) == dict):
        print(a, type(a))
        for key,val in a.items():
            print("\t{}-->{}".format(key,val))
    else:
        print(a, type(a))


#main Program
disp(10) # Function Call with int value
disp(10.2) # Function Call with float value
disp(True) # Function Call with bool value
disp(2+3j) # Function Call with complex value
print("----------------------------------------")
disp("Python")# Function Call with str value
disp(bytes([233,244,255,0,123,145]))
disp(bytearray([233,244,255,0,123,145]))
disp(range(10,21,2))
print("----------------------------------------")
disp([10,"RS",34.56,True])
disp((10,"RS",34.56,True))
print("----------------------------------------")
disp({10,"RS",34.56,True})
disp(frozenset({10,"RS",34.56,True}))
disp({1:"Python",2:"C",3:"Java",4:"DSA"})
print("----------------------------------------")
disp(None)
