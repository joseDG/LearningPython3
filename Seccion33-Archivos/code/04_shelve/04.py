import shelve

with shelve.open('data.shelve') as shelf:
    shelf['numbers'].append(1111)

with shelve.open('data.shelve', 'r') as shelf:
    for key in shelf.keys():
        print(key, shelf[key])

"""
data_cusomter (2021, '4444', ((7, 'wow'), [4, 5]))
numbers [1, 251221, 30000]

NO UPDATE

Right way: get the list. update. assign
"""
