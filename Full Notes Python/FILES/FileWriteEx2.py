#Program for Reading the Data from KBD and  Write the Data to the File
#FileWriteEx2.py
sno=int(input("Enter Student Number:"))
name=input("Enter Student Name:")
marks=float(input("Enter Student Marks:"))
#Save the students in the file--stud.info
with open("E:\\KVR-PYTHON-6PM\\FILES\\NOTES\\stud.info","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(name+"\t")
    fp.write(str(marks)+"\n")
    print("Data written to the File")
