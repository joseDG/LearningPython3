
name, age = 'mostafa', 33
print(name, 'is', age, 'years old')             # 1 old way
print(name + ' is ' + str(age) + ' years old')  # 2 old way

# The first {} is replaced with mostafa
# the 2nd is replaced with 33
print('{} is {} years old'.format(name, age))   # mostafa is 33 years old

# we call this string with curly braces {} as template


#IndexError: tuple index out of range   - u need to provide 3 arguments
#print('{}{}{}'.format('Hey'))

print('{}{}{}'.format(1, 2, 3, 4, 5, 6))    # 123 - OK to provide more. Ignored

print('{}')       # {}
print('{{}}')     # {{}}
print('{{{}}}'.format('Hey'))     # {Hey}   If you want to surround an item with {}, use double: {{ }}
#print('{{{{{{}}}}}}'.format('Hey'))      # don't :)     {{{}}}
#print('{{{{{{{}}}}}}}'.format('Hey'))    # don't :)   {{{Hey}}}

