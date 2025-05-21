#This Program converts Date into str format
#DateintoStrFmt.py
from datetime import date
# calling the today function of date class
today = date.today()
print("Today date={}  Type={}".format(today,type(today)))
# Converting the date to the string
StrDate = date.isoformat(today)
print("Today date in str={}  Type={}".format(StrDate,type(StrDate)))
