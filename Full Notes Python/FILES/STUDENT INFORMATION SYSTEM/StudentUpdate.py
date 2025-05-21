#StudentUpdate.py
import pickle
def recordupdate():
    studrecords = []
    with open("student.pick", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                studrecords.append(record)
            except EOFError:
                break
    sno=int(input("Enter Student Number for Updating Other Details"))
    #Display the records
    found=False
    for ri in range(len(studrecords)):
        if(studrecords[ri][0]==sno):
            recno=ri
            found=True
            break
    if(found):
        print("-------------------------------------")
        nsame=input("Enter New Student Name:")
        nmarks =float(input("Enter New Student Marks:"))
        ncol=input("Enter New Student College Name:")
        studrecords[recno][1]=nsame
        studrecords[recno][2] = nmarks
        studrecords[recno][3] = ncol
        print("\tRecord Updated")
        print("-------------------------------------")
        with open("student.pick","wb") as fp:
            for record in studrecords:
                pickle.dump(record,fp)
    else:
        print("\tRECORD DOES NOT EXIST")

