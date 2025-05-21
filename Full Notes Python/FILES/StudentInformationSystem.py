#StudentInformationSystem.py (Main program)
from StudentMenu import menu
from StudentAdd import recordadd
from StudentDetailsView import recordsview
while(True):
    try:
        menu()
        ch=int(input("Enter UR Choice:"))
        match(ch):
            case 1:
                recordadd()
            case 2: pass
            case 3: pass
            case 4: pass
            case 5:pass
            case 6:
                recordsview()
            case 7:
                print("Thx for Using Project")
                break
            case _:
                print("\tUR Selection of Choice is wrong-try again")
    except ValueError:
        print("\tDon't enter alnums,strs and symbols for Choice:")
