#Program for Reading the Data from CSV File
# with File Pointer Object of <class, _io.TextIOWraper>
#Non-CSVReadEx1.py
with open("E:\\KVR-PYTHON-6PM\\CSV\\NOTES\\student.csv","r") as fp:
    csvfiledata=fp.read()
    print("----------------------------------")
    print(csvfiledata)
    print("----------------------------------")

#Note: It is Not Recommended to Use File Pointer of TextIOWrapper for Reading CSV File Data
# Use csv File module