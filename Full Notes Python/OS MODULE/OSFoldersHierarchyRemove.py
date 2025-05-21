#Program for Removing the Folder---os.rmdir()
#OSFoldersHierarchyRemove.py
import os
try:
    os.removedirs("india\\ts\\HYD")
    print("Folders Hierarhcy Removed--Verify")
except FileNotFoundError:
    print("Folders Hierarhcy Does not Exist")
except OSError:
    print("U Must ensure the Specified Folders Hierarhcy Must be empty.")