#Program for Demonstrating How to Open the File
#FileOpenEx7.py
try:
    with open("kvr4.data","x+") as fp:
        print("----------------------------------")
        print("File Opened in Write mode Successfully ")
        print("Is File Closed within 'with open() as'?=", fp.closed)
        print("\tName of File=", fp.name)
        print("\tFile Mode=", fp.mode)
        print("\tIs File Readable?=", fp.readable())
        print("\tIs File Writable?=", fp.writable())
        print("----------------------------------")
    print("Is File Closed after 'with open() as'?=", fp.closed)
except FileExistsError:
    print("File already exist")