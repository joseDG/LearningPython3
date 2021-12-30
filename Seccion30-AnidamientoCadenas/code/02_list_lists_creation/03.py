

grades = [  [50, 33, 40, 30],
            [35, 50, 44, 17],
            [30, 35, 50, 37],
            [50, 35, 44, 22],
            [50, 44, 50, 30],
            [50, 36, 18, 50],
            [35, 30, 47, 16]]

# similar to slicing: this creates a new list
# BUT items are just assigned
# we call this: shallow copy
lst2 = grades.copy()

print(id(grades[0]))
print(id(lst2[0]))

# later we learn how to make deep copy
