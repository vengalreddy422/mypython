#program for Renaming a Folder--os.rename()
#OSRenameFile.py
import os
try:
    os.rename("hyd.info","hyderabad.data")
    print("File Name Renamed")
except FileNotFoundError:
    print("Source File Name Does Not Exist")