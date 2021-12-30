
from datetime import datetime

def hello1(curdate = datetime.now()):
    print(curdate)


for i in range(10):
    hello1()  # ALL of them are SAME!
    # 2021-01-11 21:36:03.142533


def hello2(curdate=None):
    if curdate is None:
        curdate = datetime.now()
    print(curdate)  # ALL of them are Different!


for i in range(10):
    hello2()

# Never use mutable or varying values as default arguments!