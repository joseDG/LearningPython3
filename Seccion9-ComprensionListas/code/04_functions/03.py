
my_list = [1, 'mostafa', 4]
for idx, item in enumerate(my_list):
    print(idx, item)
    idx = -100  # no effect
"""
0 1
1 mostafa
2 4
"""

# NOTE: this creates a complete list in memory
# Slow for a huge range
lst = list(enumerate(range(5, 9)))

for item in lst:
    print(item)
"""
(0, 5)
(1, 6)
(2, 7)
(3, 8)
"""



