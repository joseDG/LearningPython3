



def get_neibghours(i, j, cnt = 4):
    # {d, r, u, l, ul, dr, ur, dl};
    di = [1, 0, -1, 0, -1, 1, -1, 1]
    dj = [0, 1, 0, -1, -1, 1, 1, -1]

    return [(i+di[d], j+dj[d]) for d in range(cnt)]


print(get_neibghours(0, 0))
# [(1, 0), (0, 1), (-1, 0), (0, -1)]

print(get_neibghours(3, 6))
# [(4, 6), (3, 7), (2, 6), (3, 5)]

print(get_neibghours(3, 6, 8))
# [(4, 6), (3, 7), (2, 6), (3, 5), (2, 5), (4, 7), (2, 7), (4, 5)]