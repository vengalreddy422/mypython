#Program for Reading the Data from File--read()
#FileReadEx1.py
try:
    with open("E:\\KVR-PYTHON-6PM\\FILES\\NOTES\\stud.info","r") as fp:
        filedata=fp.read()
        print("---------------------------")
        print(filedata)
        print("---------------------------")
except FileNotFoundError:
    print("File Does not Exist")