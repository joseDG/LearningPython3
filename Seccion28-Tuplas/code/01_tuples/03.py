
# Same as lists

numbers = (10, 2, 7, 5, 3)

print(numbers[0], numbers[-1])  # 10 3

print(numbers[2:])    # (7, 5, 3)
print(numbers[::])    # (10, 2, 7, 5, 3)
print(numbers[::-1])  # (3, 5, 7, 2, 10)

for item in numbers:
    print(item, end=' ')    # 10 2 7 5 3

#TypeError: 'tuple' object does not support item assignment
#numbers[0] = 4

