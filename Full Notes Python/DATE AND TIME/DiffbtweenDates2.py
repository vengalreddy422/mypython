#DiffbtweenDates2.py
#--------------------------------------------------------------------
#Difference Between Two Datetime Objects
#--------------------------------------------------------------------
#To find the difference between two datetime objects, simply subtract them:
from datetime import datetime
datetime1 = datetime(2025, 3, 31)
datetime2 = datetime(2025, 4, 2)
differencedates = datetime2 - datetime1
print(differencedates)   # Output: 2 days, 20:15:25