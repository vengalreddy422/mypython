#program for Listing the Python Files in Folder.
#OSListFilesEx5.py
import os
FileNames=os.listdir("C:\\Users\\KVR\\PycharmProjects\\6PMFILESExamples")
print("Number of Files in Folder=",len(FileNames))
PythonFiles=list(filter(lambda file: file.endswith(".py"),FileNames))
for pfile in PythonFiles:
    print("\t{}".format(pfile))
print("Number of Python Files=",len(PythonFiles))