

import shelve

# let's read again

with shelve.open('data.shelve', 'r') as shelf:
    for key in shelf.keys():
        # load this specific value
        print(key, shelf[key])

"""
data (2021, '4444', ((7, 'wow'), [4, 5]))
lst [1, 251221, 30000]
data_cusomter (2021, '4444', ((7, 'wow'), [4, 5]))
numbers [1, 251221, 30000]

Surprise! Old keys exist
- the open command in writing one, load the saved files
- It doesn't remove them. just load. so old keys exist!

"""