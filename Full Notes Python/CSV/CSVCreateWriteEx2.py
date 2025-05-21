#Program for  adding the record to existing CSV File
#CSVCreateWriteEx2.py
import csv # Step-1
record=[666,"Kalyan",1.5] # Step-2
with open("E:\\KVR-PYTHON-6PM\\CSV\\NOTES\\employee.csv","a") as fp:#Step-3
    csvwr=csv.writer(fp) # Step-4
    #Here csvwr is an object of type <class, csv.writer>
    #here csvwr contains 1) writerow()  2) writerows()
    #write the single Record to CSV File
    csvwr.writerow(record) # Step-6
    print("Record added to CSV File---Verify")



