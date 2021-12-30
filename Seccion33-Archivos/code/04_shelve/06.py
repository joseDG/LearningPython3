import shelve

# let's open and delete
with shelve.open('data.shelve') as shelf:
    del shelf['data']   # make sure it exists!
    del shelf['lst']

with shelve.open('data.shelve', 'r') as shelf:
    for key in shelf.keys():
        # load this specific value
        print(key, shelf[key])

"""
data_cusomter (2021, '4444', ((7, 'wow'), [4, 5]))
numbers [1, 251221, 30000]
"""