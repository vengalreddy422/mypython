#program for Listing the Files in Folder.
#OSListFilesEx1.py
import os
FileNames=os.listdir("C:\\Users\\KVR\\PycharmProjects\\6PMFILESExamples")
for file in FileNames:
    print("\t{}".format(file))