
dict = {'x': 11, 'b': 22, 'y': 30}

print(dict.items())    # dict_items([('x', 11), ('b', 22), ('y', 30_oop)])

for key, value in dict.items():
    print(key, value)   # x 11 b 22 y 30_oop

print(dict.keys())  # dict_keys(['x', 'b', 'y'])
print(list(dict.keys()))  # ['x', 'b', 'y']

for key in dict.keys():
    print(key, dict[key])   # same, but slower (extra access)

for key in sorted(list(dict.keys())):
    print(key, dict[key])   # sorted keys: b x y

for key in sorted(dict):    # shortcut for ordered keys
    print(key, dict[key])  # sorted keys: b x y