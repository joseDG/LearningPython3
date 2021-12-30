
# Dictionary Comprehension

# without
squares = {}
for x in range(6):
    squares[x] = x*x
print(squares)

# with
squares = {x: x*x for x in range(6)}

print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}