
st1 = {1, 5, 7, 8}
st2 = {1, 5, 3, 10}

# return the set of all elements that are in st1 but not in st2
print(st1 - st2)                # {8, 7}
print(st1.difference(st2))      # same

#  return the set of all elements in either st1 or st2, but not both:
print(st1 ^ st2)    # {3, 7, 8, 10}
print(st1.symmetric_difference(st2))

# True if no intersection
print(st1.isdisjoint(st2))      # False
print(st1.isdisjoint([4, 6]))   # True