#ConvertStrDateIntoDateSecond.py
from datetime import datetime
date_str1 = "2023-08-25"
date_str2 = "2023-08-24"

datetime1 = datetime.strptime(date_str1, "%Y-%m-%d")
datetime2 = datetime.strptime(date_str2, "%Y-%m-%d")
print("Date={} Type={}".format(datetime1,type(datetime1)))
print("Date={} Type={}".format(datetime2,type(datetime1)))
difference = datetime1 - datetime2
print(difference.total_seconds())