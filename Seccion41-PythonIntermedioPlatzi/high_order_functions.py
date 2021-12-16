# estas funciones son

# Uso con filter
my_list = [1, 4, 5, 6, 9, 8, 13, 19, 21]
odd = list(filter(lambda x: x % 2 != 0, my_list))
print(odd)

# Uso con map
my_list = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, my_list))
print(squares)

# Uso con reduce
from functools import reduce

my_list = [2, 2, 2, 2, 2]  # se va multiplicando consecutivamente
all_mulplied = reduce(lambda a, b: a * b, my_list)
print(all_mulplied)
