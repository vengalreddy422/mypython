#csv file for dict write function to the file stored 
"""
writeheader()
writerows()
"""
import csv 
def dictWrite_csv():
    dct=["san","employeename","salary"]
    dct1=[{"san":10,"employeename":"ram","salary":90},
         {"san":20,"employeename":"chandra","salary":80}]
    dict2=[{"san":30,"employeename":"yaswanth","salary":90.40}]
    with open("D:\\PythonPractice\\employeerecords.csv","a") as fp:
        value=csv.DictWriter(fp,fieldnames=dct)
        value.writeheader()
        value.writerows(dct1)
        value.writerows(dict2)
        print("successfully data")
dictWrite_csv()

