



def get_neibghours(i, j):
    # {down, right, up, left};
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    return [(i+di[d], j+dj[d]) for d in range(4)]


print(get_neibghours(0, 0))
# [(1, 0), (0, 1), (-1, 0), (0, -1)]

print(get_neibghours(3, 6))
# [(4, 6), (3, 7), (2, 6), (3, 5)]
