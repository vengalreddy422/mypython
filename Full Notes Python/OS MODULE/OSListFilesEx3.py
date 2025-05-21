#program for Listing the Python Files in Folder.
#OSListFilesEx3.py
import os
FileNames=os.listdir("C:\\Users\\KVR\\PycharmProjects\\6PMFILESExamples")
print("Number of Files in Folder=",len(FileNames))
nop=0
for file in FileNames:
    if(file[-3:]==".py"):
        print("\t{}".format(file))
        nop=nop+1
else:
    print("Number of Python Files=",nop)