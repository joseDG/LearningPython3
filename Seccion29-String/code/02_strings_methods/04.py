

lst = ['a', 'bb', 'ccc']

print(''.join(lst)) # abbccc     *** most common case

print(','.join(lst)) # a,bb,ccc  *** most common case

print('#$#'.join(lst)) # a#$#bb#$#ccc

# join takes an iterable: list, string, tuple, dict, set
# join them with the used string

s1 = 'abc'
s2 = '12345'
print(s1.join(s2))  # 1abc2abc3abc4abc5

print(s2.join(s1))  # a12345b12345c