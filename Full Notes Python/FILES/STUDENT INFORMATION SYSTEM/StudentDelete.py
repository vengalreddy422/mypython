#StudentDelete.py
import pickle
def recorddelete():
    studrecords = []
    with open("student.pick", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                studrecords.append(record)
            except EOFError:
                break
    #Accept the student number to delete
    found=False
    sno=int(input("Enter Student Number to Delete Record:"))
    for recordindex in range(len(studrecords)):
        if(studrecords[recordindex][0]==sno):
            found=True
            ri=recordindex
            break
    if(found):
        studrecords.pop(ri)
        print("\tRecord Deleted")
        with open("student.pick","wb") as fp:
            for record in studrecords:
                pickle.dump(record,fp)
    else:
        print("\tRecord does not exist")
