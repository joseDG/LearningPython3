

import shelve

with shelve.open('data.shelve', 'r') as shelf:
    for key in shelf.keys():
        # load this specific value
        print(key, shelf[key])

"""
data (2021, '4444', ((7, 'wow'), [4, 5]))
lst [1, 251221, 30000]
"""