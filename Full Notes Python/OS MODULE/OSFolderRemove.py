#Program for Removing the Folder---os.rmdir()
#OSFolderRemove.py
import os
try:
    os.rmdir("D:\\Apple")
    print("Folder Removed--Verify")
except FileNotFoundError:
    print("Folder Does not Exist")
except OSError:
    print("U Must ensure the Specified Folder Must be empty.")