

import shelve

data = (2021, '4444', ((7, 'wow'), [4, 5]))
lst = [1, 251221, 30000]    # > 256

# let's open the same file.
# but we will use different keys
with shelve.open('data.shelve') as shelf:
    # Think like a dictionary. Key/value
    shelf['data_cusomter'] = data
    shelf['numbers'] = lst