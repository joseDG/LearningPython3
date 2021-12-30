

import datetime

# Constructor: hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0
dt = datetime.time(14, 7)    # 2:07 pm
print(dt)               # 14:07:00
print(dt.hour)          # 14
print(dt.minute)        # 7
print(dt.second)        # 0
print(dt.microsecond)   # 0
print(type(dt))         # <class 'datetime.time'>
print(datetime.time(14, 7, 59, 300))    # 14:07:59.000300

dt = datetime.date.today()
print(dt, type(dt))     # 2021-01-11 <class 'datetime.date'>: yyyy-mm-dd
# we can access dt.year or month or day
print(dt.ctime())       # Mon Jan 11 00:00:00 2021

