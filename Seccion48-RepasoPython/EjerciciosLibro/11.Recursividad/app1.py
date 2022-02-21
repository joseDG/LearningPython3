def print_triangle(levels):
    if levels == 0:
        return

    for i in range(0, levels):
        print("*", end='')
    print("")

    print_triangle(levels - 1)

print_triangle(6)