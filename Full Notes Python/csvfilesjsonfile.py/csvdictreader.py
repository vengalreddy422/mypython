#read the data for the dictreader of the data
import csv 
with open("D:\\PythonPractice\\employeerecords.csv","r") as fp:
    value=csv.DictReader(fp)
    for i in value:
        print(i)
    field=["san","employename","sal"]
    val=[{"san":90,"employename":"vengal","sal":9678}]
    with open("D:\\PythonPractice\\employeerecords.csv","r") as fp:
        csr=csv.DictWriter(fp,fieldnames=field)
        csr.writerow()
        csr.Writerows(val)