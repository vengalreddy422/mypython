#BaseConversioncal.py
while(True):
    s="""-------------------------------------------------------------------
                                 Base Conversion Calculator
    ---------------------------------------------------------------------
                            1.   D to B
                                 D to O
                                 D to H
                            2.   B to D
                                 B to O
                                 B to H
                            3.   O to D
                                 O to B
                                 O to H
                            4.   H to D
                                 H to B
                                 H to O
                            5. Exit
    -----------------------------------------------------------------------"""
    print(s)
    ch=int(input("Enter Ur Choice:"))
    match(ch):
        case 1:
            dv=int(input("Enter the Decimal Number System Data:"))
            bv=bin(dv)
            ov=oct(dv)
            hv=hex(dv)
            print("\tDeciaml Number System Value=",dv)
            print("\tBinary Number System Value=",bv)
            print("\tOctal Number System Value=", ov)
            print("\tHexa Decimal Number System Value=", hv)
        case 2:
            bv =input("Enter the Binary Number System Data preceded with 0b OR 0B:")
            dv=int(bv,2)
            ov = oct(dv)
            hv = hex(dv)
            print("\tBinary Number System Value=", bv)
            print("\tDeciaml Number System Value=", dv)
            print("\tOctal Number System Value=", ov)
            print("\tHexa Decimal Number System Value=", hv)
        case 3:
            ov = input("Enter the Octal Number System Data preceded with 0o OR 0O:")
            dv = int(ov, 8)
            bv = bin(dv)
            hv = hex(dv)
            print("\tOctal Number System Value=", ov)
            print("\tDeciaml Number System Value=", dv)
            print("\tBinary Number System Value=", bv)
            print("\tHexa Decimal Number System Value=", hv)
        case 4:
            hv = input("Enter the Hexa Number System Data preceded with 0x OR 0X:")
            dv=int(hv,16)
            bv=bin(dv)
            ov=oct(dv)
            print("\tHexa Decimal Number System Value=", hv)
            print("\tDeciaml Number System Value=", dv)
            print("\tBinary Number System Value=", bv)
            print("\tOctal Number System Value=", ov)
        case 5:
            print("Thx for Using Project")
            break
        case _:
            print("UR Selection of Operation is wrong-try again")
