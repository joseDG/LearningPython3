

def from2d_to_1d(cols, i, j):
    return i * cols + j


def from1d_to_2d(cols, idx):
    return idx//cols, idx % cols


def list_relations(rows = 3, cols = 5):
    idx = 0
    for r in range(rows):
        for c in range(cols):
            print(f'({r}, {c}) ==> {idx}')

            assert (r, c) == from1d_to_2d(cols, idx)
            assert idx == from2d_to_1d(cols, r, c)

            idx += 1


list_relations(3, 5)