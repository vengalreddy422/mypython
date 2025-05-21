#Program for Demonstrating How to Open the File
#FileOpenEx4.py
try:
    with open("kvr1.data","r") as fp:
        print("----------------------------------")
        print("File Opened in Read mode Successfully ")
        print("\tName of File=",fp.name)
        print("\tFile Mode=",fp.mode)
        print("\tIs File Closed within 'with open() as'?=", fp.closed)
        print("\tIs File Readable?=",fp.readable())
        print("\tIs File Writable?=", fp.writable())
        print("----------------------------------")
except FileNotFoundError:
    print("File does not Exist")
