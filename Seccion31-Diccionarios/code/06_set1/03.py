
st = {(1, 5), (2, 7), (1, 5), (2, 7)}
print(st)   # {(2, 7), (1, 5)}

# TypeError: unhashable type: 'list'
#st = {(1, 5), [2, 7]}

print(len(st))  # 2
print(max(st))  # (2, 7)
print(sorted(st))  #[(1, 5), (2, 7)]

print(sum({1, 1, 1, 1, 2, 2, 2, 2}))    # 3 = 1+2
print(all({1, 2, 'hey'}))       # True
print(all({1, 2, 'hey', ()}))   # False: empty tuple