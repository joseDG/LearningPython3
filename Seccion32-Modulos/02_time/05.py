import time     # for .sleep
from time import perf_counter

start_time = perf_counter()

for i in range(5):
    print(i)
    time.sleep(1)   # hang for 1 second

end_time= perf_counter()
time_dif = end_time - start_time
print(time_dif)    # 5.003786797984503

# perf_counter_ns(): Py3.7: return time as nanoseconds
