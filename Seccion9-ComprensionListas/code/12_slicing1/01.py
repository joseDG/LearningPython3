
# [First index to include, first index to exclude : step]
# step can be +ve or -ve
# range can be increasing or decreasing based on step

print(type(range(5)))

print(list(range(5)))               # [0, 1, 2, 3, 4]

print(list(range(2, 5)))            # [2, 3, 4]

print(list(range(1, 21, 4)))        # [1, 5, 9, 13, 17]

print(list(range(5, 0, -1)))        # [5, 4, 3, 2, 1]

print(list(range(10, 0, -2)))       # [10, 8, 6, 4, 2]

print(list(range(5-1, -1, -1)))     # [4, 3, 2, 1, 0]