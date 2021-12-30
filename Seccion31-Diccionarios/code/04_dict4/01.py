

dict = {'x': 11, 'b': 22, 'y': 30}
dict['a'] = 33

dict.update({'aaa':3, 'b':-2})  # merge
print(str(dict)) # {'x': 11, 'b': -2, 'y': 30_oop, 'a': 33, 'aaa': 3}
# you can pass dict or list of tuples

print(len(dict))    # 5

# True if all keys are trye
print(all(dict))    # True
dict[''] = "hey"
print(all(dict))    # False
print(any(dict))    # True
