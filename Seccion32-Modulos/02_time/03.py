import time


if __name__ == '__main__':
    tm = time.localtime()

    # method returns a string representing date and time
    print(time.strftime('%m/%d/%Y, %H:%M:%S', tm))  # 01/17/2021, 11:03:55
    print(time.strftime('%H-%M-%S', tm))            # 11-03-55
    print(time.strftime('%M', tm))                  # 03
    print(time.strftime('%c', tm))                  # Sun Jan 17 11:07:55 2021

    cur_time = time.time()
    print(time.strftime('%S', time.localtime(cur_time)))    # 55

    print(time.strftime('%R', tm))  # time in 24 hour notation
    # It is also available from datetime object
    # There are more options: read docs strftime
    