#Program for Creating a CSV File
#CSVCreateWriteEx1.py
import csv # Step-1
colnames=["EMPNO","NAME","SAL"] # Step-2
records=[[111,"SrinuSri79",1.2],
        [222,"Pavan",1.2],
        [333,"Charan",1.5],
        [444,"KVR",0.0],
        [555,"Sharshad",1.3]] # Step-3
with open("E:\\KVR-PYTHON-6PM\\CSV\\NOTES\\employee.csv","a") as fp:#Step-4
    csvwr=csv.writer(fp) # Step-5
    #Here csvwr is an object of type <class, csv.writer>
    #here csvwr contains 1) writerow()  2) writerows()
    #write the column names to CSV File
    csvwr.writerow(colnames) # Step-6
    #write reacords to the CSV File
    csvwr.writerows(records) # Step-7
    print("CSV File Created---Verify")



