

if __name__ == '__main__':
    # flip every separator to a space, then trivially split and sort
    # input() reads a line
    # .replace(',', ' ')  return a string with replacements
    # consective .replace is applied on return
    # then .split on a string with just spaces
    # then sorted over the returned list
    # then print over the list argument
    print(sorted(input().replace(',', ' ').replace('$', ' ').replace('#', ' ').split()))

    # I am coding it this way for educational purpose
    # In practice: you should divide the code to a few lines



# apple,banana, , , apple,student### #student$$apple