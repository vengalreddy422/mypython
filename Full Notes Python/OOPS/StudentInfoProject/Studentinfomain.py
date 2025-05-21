
from  menu import Menu
from Addstudent import Insertstudent
from ViewRecord import View
from SearchStudentRecord import Searchstudent
from DeleteStudentData import Deleterecord
from UpdateStudentDetails import Update
s=Menu()
s1=Insertstudent()
record=View()
search=Searchstudent()
delete=Deleterecord()
s2=Update()

while(True):

    s.studentmenu()
    try:
        ch=int(input("Enter Your Choice:"))
        match(ch):
            case 1:
                s1.savestuddata()
            case 2:
                s2.updateRecord()
            case 3:
                delete.removerecord()
            case 4:
                search.serchstudentrecord()
            case 5:
                record.veiwrecord()
            case 6:
                record.veiwrecords()
            case 7:
                print("\tThx for using this Project")
                break
            case _:
                print("\tUr Choice is wrong try-again")
    except ValueError:
        print("\tDon't enter strs,alnums and symbol for choice")

