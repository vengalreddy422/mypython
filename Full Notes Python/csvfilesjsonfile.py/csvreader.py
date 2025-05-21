#csv of the read the data
import csv
with open("D:\\PythonPractice\\employeerecords.csv","r") as fp:
    value=csv.reader(fp)
    for i in value:
        print(i,end="")