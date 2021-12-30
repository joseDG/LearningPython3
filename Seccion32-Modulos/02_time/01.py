
import time

if __name__ == '__main__':
    # Convert seconds since the Epoch to a time tuple expressing UTC (GMT)
    # The epoch is the point where the time starts
    # Platoform dependent: Unix, the epoch is January 1, 1970, 00:00:00 UTC (GMT)
    print(time.gmtime(0))

    print(time.localtime())
    # time.struct_time(tm_year=2021, tm_mon=1, tm_mday=17, tm_hour=9, tm_min=43,
    #   tm_sec=7, tm_wday=6, tm_yday=17, tm_isdst=0)
    print(time.localtime().tm_hour)  # 9
    print(time.localtime()[3])       # 9 - access the object using index

    print(time.time())  # 1610905180.9765534
    # [we are in 2021 - 1970 = 51 years => ~51*365*24*60*60



