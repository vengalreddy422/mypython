#DiffbtweenDates.py
from datetime import datetime
td = datetime.now()
past = datetime(2022, 4, 2, 19, 3, 0)  # Example past date
difference = td - past
print(difference)    # 
print(type(difference))