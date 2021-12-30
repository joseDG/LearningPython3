
lst = [1, 2, 3]
print(id(lst))      # 0x111
lst += [4]          # in-place change     - internally: __iadd__
print(id(lst))      # 0x111
lst = lst + [5]     # NEW memory creation - internally: __add__
print(id(lst))      # 0x222

# += is behaving similar to .extend

lst += ['Hey']  # iterate on list: add 1 item
print(lst)      # [1, 2, 3, 4, 5, 'Hey']

lst += 'Hey'    # iterate and add 3 items
print(lst)      # [1, 2, 3, 4, 5, 'Hey', 'H', 'e', 'y']

#TypeError: can only concatenate list (not "str") to list
#lst = lst + 'Hey'
#lst = lst + 10
