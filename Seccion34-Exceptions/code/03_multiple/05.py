
try:
    path, idx = input().split()
    idx = int(idx)

    with open(path, 'r') as file:
        lst = file.read().splitlines()
        print(lst[idx])
        # File will ALWAYS be closed
except BaseException as e:      # same as except without class
    # as e: e is the created exception object
    error = str(e)  # get the error msg
    print(error)
