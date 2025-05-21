#Program for Reading the Data from File--read()
#FileReadEx2.py
try:
    with open("E:\\KVR-PYTHON-6PM\\FILES\\NOTES\\stud.info","r") as fp:
        filedata=fp.readlines()
        print("---------------------------")
        for record in filedata:
            print(record,end="")
        print("---------------------------")
except FileNotFoundError:
    print("File Does not Exist")