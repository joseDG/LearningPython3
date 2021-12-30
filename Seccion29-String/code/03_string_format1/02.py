
name, age = 'mostafa', 33

print('{0} is {1} years old'.format(name, age))     # mostafa is 33 years old

#print('{0} is {2} years old'.format(name, age))     # IndexError - no idx 2

print('{0} is {1} years old. Are you {1} years as {0}'.format(name, age))
# mostafa is 33 years old. Are you 33 years as mostafa
# pros: you provie positional argument once and use it many

print('{name} is {AGE} years old. Are you {AGE} years as {name}'.format(name=name, AGE=age))
# mostafa is 33 years old. Are you 33 years as mostafa
# similarly, we can use keyword arguments but flxible order!

# Be careful from mixing
print('{} is {age} years old'.format(name, age=age))    # mostafa is 33 years old
print('{0} is {age} years old'.format(name, age=age))   # mostafa is 33 years old

#print('{1} is {age} years old'.format(age=age, name))
# SyntaxError: positional argument follows keyword argument
#print('{1} is {age} years old'.format(name, age=age))   # IndexError

