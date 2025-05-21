#program for Listing the Python Files in Folder.
#OSListFilesEx4.py
import os
FileNames=os.listdir("C:\\Users\\KVR\\PycharmProjects\\6PMFILESExamples")
print("Number of Files in Folder=",len(FileNames))
for file in FileNames:
    if(file.startswith("OS")):
        print("\t{}".format(file))
