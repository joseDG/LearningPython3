import time

start_time = time.time()

for i in range(5):
    print(i)
    time.sleep(1)   # hang for 1 second

end_time= time.time()
time_dif = end_time - start_time
print(time_dif)    # 5.003431558609009

