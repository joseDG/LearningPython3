

a = [1, 2, 20, 6, 210, 2, 1]
d = dict.fromkeys(a)
# {1: None, 2: None, 20: None, 6: None, 210: None}

print(dict.fromkeys(a, 7))
# {1: 7, 2: 7, 20: 7, 6: 7, 210: 7}

unique_keys = dict.fromkeys(a).keys()
print(unique_keys)   # dict_keys([1, 2, 20, 6, 210])
# removed duplicated + preserved the order

unique_keys = list({10:2, 1:5})
print(unique_keys)  # [10, 1]

