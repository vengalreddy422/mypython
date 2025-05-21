#Program for Reading the Data from KBD and  Write the Data to the File
#FileWriteEx4.py
print("Enter the Information from KBD (Press @ to Stop):")
with open("hyd.info","a") as fp:
    while(True):
        kbdata=input()
        if(kbdata!="@"):
            fp.write(kbdata+"\n")
        else:
            print("Data written to the file--verify")
            break


