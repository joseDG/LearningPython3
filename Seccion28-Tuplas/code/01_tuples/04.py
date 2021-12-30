

numbers = (10, 2, 7, 2, 2, -5)

print(numbers.count(2))     # 3
print(numbers.index(2))     # 1

#AttributeError: 'tuple' object has no attribute 'remove'
#numbers.remove(0)

#TypeError: 'tuple' object doesn't support item deletion
#del numbers[0]

print(min(numbers), max(numbers))   # -5 10

lst = sorted(numbers)   # LIST: [-5, 2, 2, 2, 7, 10]

print(tuple(sorted(numbers))) #   (-5, 2, 2, 2, 7, 10)
print(tuple(reversed(numbers))) # (-5, 2, 2, 7, 2, 10)

