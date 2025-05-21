#ProgrammerChoiceValueConvert.py
pv=input("Enter Ur Value of Number System:")
if(pv.startswith("0b") or pv.startswith("0B")):
    print("Binary Value:{}".format(pv))
    print("\tDec({})={}".format(pv,int(pv,2)))
    print("\tOct({})={}".format(pv, oct(int(pv, 2))))
    print("\tHex({})={}".format(pv, hex(int(pv, 2))))
elif(pv.startswith("0o") or pv.startswith("0O")):
    print("Octal Value:{}".format(pv))
    print("\tDec({})={}".format(pv, int(pv, 8)))
    print("\tBin({})={}".format(pv, bin(int(pv, 8))))
    print("\tHex({})={}".format(pv, hex(int(pv, 8))))
elif(pv.startswith("0x") or pv.startswith("0X")):
    print("Hexa Decimal Value:{}".format(pv))
    print("\tDec({})={}".format(pv, int(pv, 16)))
    print("\tBin({})={}".format(pv, bin(int(pv, 16))))
    print("\tOct({})={}".format(pv, oct(int(pv, 16))))
elif( not pv.startswith("0")):
    print("Decimal Value:{}".format(pv))
    print("\tBin({})={}".format(pv, bin(int(pv))))
    print("\tOct({})={}".format(pv, oct(int(pv))))
    print("\tHex({})={}".format(pv, hex(int(pv))))
else:
    print("{} is Invalid Decimal Value".format(pv))

