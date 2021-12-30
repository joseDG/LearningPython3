

my_str = 'mostafa'

# TypeError: 'str' object does not support item assignment
#my_str[3] = 'T'        #immutable!

my_str = my_str[:3] + my_str[3].upper() + my_str[4:]
print(my_str)   # mosTafa

my_str2 = my_str
print(my_str is my_str2)        # True

print(id(my_str))   # 0x111
my_str += ' saad'

print(id(my_str))   # 0x222
print(id(my_str2))  # 0x111

print(my_str is my_str2)        # False


