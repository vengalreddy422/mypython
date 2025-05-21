#Program for Reading CSV File Data
#CSVReadEx1.py
import csv
try:
    with open("E:\\KVR-PYTHON-6PM\\CSV\\NOTES\\citizen.csv","r") as fp:
        csvr=csv.reader(fp)
        for record in csvr:
            for val in record:
                print("{}".format(val),end="\t")
            print()
except FileNotFoundError:
    print("CSV File Does Not Exist")