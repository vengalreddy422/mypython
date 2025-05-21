#Program for Removing the File Name
#OSRemovingFileName.py
import os
try:
    os.remove("D:\\index.kvr")
    print("File Removed--verify")
except FileNotFoundError:
    print("File Does Not Exist")