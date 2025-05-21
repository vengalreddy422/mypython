#Program for Demonstrating How to Open the File
#FileOpenEx1.py
try:
    fp=open("kvr1.data","r")
except FileNotFoundError:
    print("File Does not Exist")
else:
    print("----------------------------------")
    print("Type of fp=", type(fp))
    print("File Opened in Read mode Successfully ")
    print("Is File Closed?=",fp.closed )
    print("----------------------------------")
finally:
    print("---------Outer finally------------------------")
    print("I am from finally Block")
    try:
        fp.close()
    except NameError:
        print("File Not at all existing-No Need to Close")
    finally:
       print("---------nested finally-------------------------")
       fp.close()
       print("Is File Closed after close()?=", fp.closed)
