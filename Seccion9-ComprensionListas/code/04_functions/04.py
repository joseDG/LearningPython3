
# all: Return True if all elements of the iterable are true
lst = [10, 20, -12, 'Mostafa']

print(all(lst))     # True
print(all([]))      # True

# items cause Faulse
print(all([False]))     # False
print(all(['']))        # False
print(all([0]))         # False

print(all([10, 0, 2]))        # False

# Return True if any element of the iterable is true
lst = [10, 20, 0, 'Mostafa']

print(all(lst))     # False
print(any([]))      # True

