

dct1 = {'A': 10, 'B': 20}
dct2 = {'C': 30, 'D': 40}

print(*dct1)    # A B


# merging dictionaries
dct = {**dct1, **dct2}
print(dct)
# {'A': 10, 'B': 20, 'C': 30, 'D': 40}
