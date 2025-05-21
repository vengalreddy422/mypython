#program for Renaming a Folder--os.rename()
#OSRenameFolder.py
import os
try:
    os.rename("KVR","PYTHON")
    print("Folder Renamed")
except FileNotFoundError:
    print("Source Folder Does Not Exist")