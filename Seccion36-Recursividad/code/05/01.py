

def print_triangle(levels):
    if levels == 0:
        return

    print_triangle(levels - 1)

    for i in range(0, levels):
        print("*", end='')
    print("")


print_triangle(5)