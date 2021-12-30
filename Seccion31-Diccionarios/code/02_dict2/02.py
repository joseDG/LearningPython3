
dict = {
    int: [6, 9, 10],
    float : 10,
    6: 20,
    6: 70,
    6: 80,
}
print(dict[float])  # 10    observe we can use data types, as they are immutable
print(dict[6])      # 80    mutliple same keys: last value is used
#print(dict[7])      # KeyError: 7

# setdefault: returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value
print(dict.setdefault(6, -8))   # 80
print(dict.setdefault(7, 20))   # 20
print(dict[7])      # 20