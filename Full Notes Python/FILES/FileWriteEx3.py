#Program for Saving the Iterable Object Data into the File
#FileWriteEx3.py
x={10:"Python",20:"C",30:"Java",40:"OS"}
with open("itstud.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data written to the File")
