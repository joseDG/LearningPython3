import time

if __name__ == '__main__':
    # strptime() method creates a datetime object from the given string.
    tm = time.localtime()
    string = time.strftime('%c', tm)
    print(string)       # Sun Jan 17 11:07:55 2021

    tm2 = time.strptime(string)
    print(tm2.tm_hour)  # 11

    # strptime is short for "parse time"
    # strftime is short for "formatting time".
    # They are opposite functionalities

