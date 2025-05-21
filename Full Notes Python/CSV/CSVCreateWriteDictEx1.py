#Program for Creating CSV File With Dict Data.
#CSVCreateWriteDictEx1.py
import csv # Step-1
colnames=["CID","CNAME","ADDR"] # Step-2
records=[{"CID":100,"CNAME":"Mansi","ADDR":"MH"},
         {"CID":200,"CNAME":"Uma","ADDR":"TS"},
         {"CID":300,"CNAME":"Prajwala","ADDR":"MH"},
         {"CID":400,"CNAME":"Sneha","ADDR":"AP"}] # Step-3
with open("E:\\KVR-PYTHON-6PM\\CSV\\NOTES\\citizen.csv","a") as fp: # Step-4
    csvdwr=csv.DictWriter(fp,fieldnames=colnames) #  Step-5
    # Here csvdwr is an object of type <class, csv.Dictwriter>
    # here csvdwr contains 1) writeheader()  2) writerows() 3) writerow()
    # write the column names to CSV File
    csvdwr.writeheader() #  Step-6
    # write reacords to the CSV File
    csvdwr.writerows(records) # Step-7
    print("CSV File Created with Dict data--verify")




