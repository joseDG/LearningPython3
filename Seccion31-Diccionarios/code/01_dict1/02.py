
# The key can be from ANY IMMUTABLE value
# This what make dict very useful

dict = {'a' : 'alpha',  # key:value
        'o': 'omega',
        'g': 'gamma'
        }
print(dict)
# {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
print(dict.keys())
# dict_keys(['a', 'o', 'g'])
print(dict.values())
# dict_values(['alpha', 'omega', 'gamma'])

print(dict['a'])    # alpha