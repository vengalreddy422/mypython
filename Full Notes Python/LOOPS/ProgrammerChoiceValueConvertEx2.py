#ProgrammerChoiceValueConvert2.py
pv=input("Enter Ur Value of Number System:").strip()
if(pv.startswith("0b") or pv.startswith("0B")):
    data=pv[2:]
    res=True
    for val in data:
        if(int(val) not in [0,1]):
            res=False
            break
    if(res):
        print("Binary Value:{}".format(pv))
        print("\tDec({})={}".format(pv, int(pv, 2)))
        print("\tOct({})={}".format(pv, oct(int(pv, 2))))
        print("\tHex({})={}".format(pv, hex(int(pv, 2))))
    else:
        print("{} is invalid Binary data".format(pv))
elif(pv.startswith("0o") or pv.startswith("0O")):
    data = pv[2:]
    res = True
    for val in data:
        if (int(val) not in range(0,8)):
            res = False
            break
    if (res):
        print("Octal Value:{}".format(pv))
        print("\tDec({})={}".format(pv, int(pv, 8)))
        print("\tBin({})={}".format(pv, bin(int(pv, 8))))
        print("\tHex({})={}".format(pv, hex(int(pv, 8))))
    else:
        print("{} is invalid Octal data".format(pv))

elif(pv.startswith("0x") or pv.startswith("0X")):
    data = pv[2:]
    res = True
    for val in data:
        if( (val not in ['0','1','2','3','4','5','6','7','8','9']) and (val.upper() not in list("ABCDEF"))):
            res = False
            break
    if (res):
        print("Hexa Dec Value:{}".format(pv))
        print("\tDec({})={}".format(pv, int(pv, 16)))
        print("\tBin({})={}".format(pv, bin(int(pv, 16))))
        print("\tOct({})={}".format(pv, oct(int(pv, 16))))
    else:
        print("{} is invalid Hexa Dec data".format(pv))
elif( not pv.startswith("0") and pv.isdigit()):
    print("Decimal Value:{}".format(pv))
    print("\tBin({})={}".format(pv, bin(int(pv))))
    print("\tOct({})={}".format(pv, oct(int(pv))))
    print("\tHex({})={}".format(pv, hex(int(pv))))

else:
    print("{} is Invalid Decimal Value".format(pv))

