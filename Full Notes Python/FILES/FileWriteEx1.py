#Program for Writing the Data to the File
#FileWriteEx1.py
sno=300
sname="Ricthe"
marks=36.78
with open("student.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data Written to File--verify")

