

grades = [  [1, 2, 3, 4],
            [5, 6],
            [7, 8, 9, 10, 11]
        ]

for a, b, c in zip(*grades):
    print(a, b, c)

"""
1 5 7
2 6 8

unpacking + zip Allowing us to iterate on coulmns
"""
