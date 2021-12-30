

import shelve

data = (2021, '4444', ((7, 'wow'), [4, 5]))
lst = [1, 251221, 30000]    # > 256

# By default, the underlying database
# file is opened for reading and writing
with shelve.open('data.shelve') as shelf:
    # Think like a dictionary. Key/value
    shelf['data'] = data
    shelf['lst'] = lst
    #Use strings as keys
    #shelf[10] = 20 # 'int' object has no attribute 'encode'