


grades = [  [1, 2, 3, 4],
            [5, 6],
            [7, 8, 9, 10, 11],   # observe the last comma is ok
        ]

print(len(grades))        # 3: the list has 3 items: each is a list
print(len(grades[0]), len(grades[1]), len(grades[2]))   # 4 2 5

# lists are mutable: we can change content
print(grades[1][0])     # 5
grades[1][0] = 100
print(grades[1][0])     # 100




