#Program for Copying the Content of One File to Another File
#FileCopy.py
def filecopy():
    try:
        srcfile=input("Enter Source File:")
        with open(srcfile,"r") as rp:
            dstfile=input("Enter Destination File:")
            with open(dstfile,"a") as wp:
                #read the Data from Source File
                srcfiledata=rp.read()
                #write srcfiledata to Destination file
                wp.write(srcfiledata)
                print("File Copied--verify")
    except FileNotFoundError:
        print("Source File Does not Exist")

#main Program
filecopy() # Fucntion call