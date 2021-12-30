
try:
    path, idx = input().split()
    idx = int(idx)

    file = open(path, 'r')
    lst = file.read().splitlines()
    print(lst[idx])

    file.close()

except (ValueError, IndexError):    # observe ()
    print('ValueError or IndexError')
except FileNotFoundError:
    print('FileNotFoundError')
except:
    print('Something else')

#For both ValueError or IndexError => one handling

