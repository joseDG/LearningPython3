
if __name__ == '__main__':
    rows, cols, *commands = input().split()
    rows, cols = int(rows), int(cols)

    # up, right, down, left
    rd = [-1, 0, 1, 0]
    cd = [0, 1, 0, -1]
    r, c = 0, 0

    while commands:
        dir, steps, *commands = commands
        dir = ['up', 'right', 'down', 'left'].index(dir)    # index of direction
        steps = int(steps)
        # as we circulate, then the % can help removing unnecessary cycles, regardless how big
        r = (r + rd[dir] * steps) % rows
        c = (c + cd[dir] * steps) % cols
        print(r, c)


