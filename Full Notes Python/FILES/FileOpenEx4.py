#Program for Demonstrating How to Open the File
#FileOpenEx4.py
with open("kvr2.data","a+") as fp:
    print("----------------------------------")
    print("File Opened in Write mode Successfully ")
    print("Is File Closed within 'with open() as'?=", fp.closed)
    print("\tName of File=", fp.name)
    print("\tFile Mode=", fp.mode)
    print("\tIs File Readable?=", fp.readable())
    print("\tIs File Writable?=", fp.writable())
    print("----------------------------------")
print("Is File Closed after 'with open() as'?=", fp.closed)