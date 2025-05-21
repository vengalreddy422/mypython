#Program for Demonstrating How to access the Data of the File Randomly.
#FilePointer.tell()-->Gives Index of File Pointer where It points
#FilePointer.seek()-->It will Re-Set the File Pointer to the Perticual Index.
#RandomAccessFileEx1.py
with open("hyd.info","r") as fp:
    print("--------------------------------")
    print("Initial Position of fp=",fp.tell()) # 0
    filedata=fp.read(5)
    print("File Data=",filedata)
    print("Now Position of fp=", fp.tell())  # 5
    print("--------------------------------")
    filedata = fp.read(5)
    print("File Data=", filedata)
    print("Now Position of fp=", fp.tell())  # 10
    print("--------------------------------")
    filedata = fp.read(6)
    print("File Data=", filedata)
    print("Now Position of fp=", fp.tell())  # 16
    print("--------------------------------")
    filedata = fp.read()
    print("File Data=", filedata)
    print("Now Position of fp=", fp.tell())  #106
    print("--------------------------------")
    filedata = fp.read()
    print("File Data=", filedata)
    print("Now Position of fp=", fp.tell())  #106
    print("--------------------------------")
    #Re-set the File Pointer to 10th Index
    fp.seek(10)
    filedata = fp.read(6)
    print("File Data=", filedata)
    print("Now Position of fp=", fp.tell())  # 16
    print("--------------------------------")
    # Re-set the File Pointer to 0th Index
    fp.seek(0)
    filedata = fp.read(16)
    print("File Data=", filedata)
    print("Now Position of fp=", fp.tell())  # 16
    print("--------------------------------")
