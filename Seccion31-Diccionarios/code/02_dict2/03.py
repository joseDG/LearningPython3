
dict = {
    -1200001 : 'mostafa',
    'ziad' : 25.5,
    (4, 6) : [5, 8, 9],
}

print('ziad' in dict)   # True
print(100 in dict)      # False

#if dict[7] == 5:    # KeyError: 7
#    pass

if 7 in dict and dict[7] == 5:
    pass    # short-circuit evaluation

