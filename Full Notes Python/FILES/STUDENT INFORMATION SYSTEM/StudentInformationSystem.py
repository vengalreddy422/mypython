#StudentInformationSystem.py (Main program)
from StudentMenu import menu
from StudentAdd import recordadd
from StudentDetailsView import recordsview,recordview
from StudentSearch import recordsearch
from StudentDelete import recorddelete
from StudentUpdate import recordupdate
while(True):
    try:
        menu()
        ch=int(input("Enter UR Choice:"))
        match(ch):
            case 1:
                recordadd()
            case 2:
                recorddelete()
            case 3:
                recordupdate()
            case 4:
                recordsearch()
            case 5:
                recordview()
            case 6:
                recordsview()
            case 7:
                print("Thx for Using Project")
                break
            case _:
                print("\tUR Selection of Choice is wrong-try again")
    except ValueError:
        print("\tDon't enter alnums,strs and symbols for Choice:")
