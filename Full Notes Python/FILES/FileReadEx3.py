#Program for accepting the File Name and display Its Content.
#FileReadEx3.py
try:
    filename=input("Enter File Name to View Its Content:")
    with open(filename,"rt") as fp:
        filedata=fp.readlines()
        print("---------------------------")
        for record in filedata:
            print(record,end="")
        print("---------------------------")
except FileNotFoundError:
    print("File Does not Exist")