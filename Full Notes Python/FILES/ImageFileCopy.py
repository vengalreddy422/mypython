#Program for Copying  the Iamge
#ImageFileCopy.py
def filecopy():
    try:
        with open("D:\\SUB\\kvr.png","rb") as rp:
            with open("pf.png","wb") as wp:
                #read the Data from Source File
                srcfiledata=rp.read()
                #write srcfiledata to Destination file
                wp.write(srcfiledata)
                print("Image Copied--verify")
    except FileNotFoundError:
        print("Source File Does not Exist")

#main Program
filecopy() # Fucntion call