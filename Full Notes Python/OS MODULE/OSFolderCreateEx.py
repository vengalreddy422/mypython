#Program for Creating a folder-----we use  mkdir() of os module
#OSFolderCreateEx.py
import os
try:
    os.mkdir("KVR")
    print("Folder Created--verify")
except FileExistsError:
    print("Folder already created")
except FileNotFoundError:
    print("File Does not Exist")