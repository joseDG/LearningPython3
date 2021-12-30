
dict = {
    -1200001 : 'mostafa',
    'ziad' : 25.5,
    (4, 6) : [5, 8, 9],
}

print(dict.get(7))          # None
print(dict.get(7, 15))      # 15    (return default val if not exist)
print(7 in dict)            # False
print(dict.get((4, 6)))     # [5, 8, 9]

dict.clear()       # remove all keys

