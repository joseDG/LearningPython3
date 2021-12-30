
file = None
try:
    path, idx = input().split()
    idx = int(idx)

    file = open(path, 'r')
    lst = file.read().splitlines()
    print(lst[idx])

except OSError: # cover all sub-types
    print('Catch all OS errors')
except:
    print('Something else')

finally:
    # In all previous codes we wrongly handled it
    if file is not None:
        file.close()
