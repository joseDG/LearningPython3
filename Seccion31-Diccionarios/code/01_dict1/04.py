
# Dict is mutable. We can update its content
dict = {}   # No initial value
dict[12] = [405, (1, 'mostafa')]    # Add a new key-value
dict['mostafa'] = 20

print(dict[12]) # [405, (1, 'mostafa')]
dict[12] = 'hello'
print(dict[12]) # hello
print(dict.keys())  # dict_keys([12, 'mostafa'])

del dict[12]
print(dict.keys())  # dict_keys(['mostafa'])
#print(dict[12])    # KeyError: 12

dict[12] = 10
dict[12] += 5
print(dict[12])    # 15
print(dict.pop(12)) # 15 : get and remove
print(dict.pop('hey', 37))  # 37 default value
