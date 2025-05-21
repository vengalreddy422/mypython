#StudentSearch.py<----File Name and Module Name
import pickle
def recordsearch():
    studrecords = []
    with open("student.pick", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                studrecords.append(record)
            except EOFError:
                break
        # Accept the Student Number and Display the Details
        sno = int(input("Enter Student Number to Search:"))
        found = False
        for record in studrecords:
            if (record[0] == sno):
                found = True
                break
        print("--------------------------------------")
        if (found):
            print("\tSTUDENT RECORD EXIST")
        else:
            print("\tSTUDENT RECORD DOES NOT EXIST")
        print("--------------------------------------")

