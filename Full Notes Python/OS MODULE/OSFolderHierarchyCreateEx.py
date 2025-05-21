#Program for Creating a folders Hierarchy-----we use  makedirs() of os module
#OSFolderHierarchyCreateEx.py
import os
try:
    os.makedirs("D:\\INDIA\\TS\\HYD")
    print("Folder Hierarchy Created--verify")
except FileExistsError:
    print("Folders Hierarchy already Exist ")