#Program for Reading CSV File Data
#CSVDictReadEx1.py
import csv
with open("E:\\KVR-PYTHON-6PM\\CSV\\NOTES\\citizen.csv","r") as fp:
    csvdr=csv.DictReader(fp)
    for record in csvdr:
        for key,val in record.items():
            print("\t{}-->{}".format(key,val))
        print("--------------------------------")