elements = [
    [1, 4, 6, 7],
    [4, 5, 6],
    [6, 7, 8],
    [],
    ["nodata", "nodata"],
    [1, 3]
            ]

for e in elements:
    if e and isinstance(e[0], int):
        print(e[0])