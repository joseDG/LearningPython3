
def list_relations(depth = 3, rows = 4, cols = 5):
    idx = 0
    for d in range(depth):
        for r in range(rows):
            for c in range(cols):
                print(f'({d}, {r}, {c}) ==> {idx}')
                idx += 1

if __name__ == '__main__':
    depth, rows, cols, type, *remain = map(int, input().split())
    db = rows * cols    # a single depth block
    rb = cols           # a single r block (cols value)
    cb = 1              # a single column block (single value)

    if type == 1:
        d, r, c = remain
        idx = d * db + r * rb + c * cb
        print(idx)
    else:
        idx = remain[0]
        # r * Rb + c * 1 < Db
        d = idx // db
        # Remove d part, then extract r
        r = (idx % db) // rb
        c = (idx % db) % rb
        print(d, r, c)
