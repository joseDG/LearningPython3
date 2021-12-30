# fstring is the modern way

name, age = 'mostafa', 33

# mostafa is 33 years old
print('{} is {} years old'.format(name, age))
print('{name} is {age} years old'.format(name=name, age=age))

print(f'{name} is {age} years old')


val = 71.0123456789012345678901234

#     71.012
print('{:11.3f}'.format(val))
print(f'{val:11.3f}')