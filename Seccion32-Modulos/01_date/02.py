
import datetime

dt = datetime.datetime(2021, 1, 11, 14, 7, 59, 300)
# or use
print(dt.ctime())       # Mon Jan 11 14:07:59 2021

newdt = dt.replace(year=1990, day=25, second=13)
print(newdt)    # 1990-01-25 14:07:59.000300

delta = dt - newdt
print(delta, type(delta))   # 111309 days, 0:00:46 <class 'datetime.timedelta'>
print(delta.seconds)            # 46
print(delta.total_seconds())    # 977097646

# immutables