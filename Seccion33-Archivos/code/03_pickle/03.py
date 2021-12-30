

import pickle

with open("data.pickle", "rb") as pickle_file:
    data = pickle.load(pickle_file)
    lst = pickle.load(pickle_file)
    print(data)
    print(lst)

"""
(2021, '4444', ((7, 'wow'), [4, 5]))
[1, 2, 3]
"""

# Observe: we read/write full thing
# Always overwrite
# Try to corrupt and read