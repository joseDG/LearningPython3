# another perspective

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Positive step: Missing start: iterate from the begin
print(my_list[ :5:1])       # [0, 1, 2, 3, 4]

# Positive step: Missing end: iterate till the end (inclusive)
print(my_list[2: :1])       # [2, 3, 4, 5, 6, 7, 8]

# Negative step: Missing start: iterate from the end
print(my_list[ :5:-1])      # [8, 7, 6]

# Negative end: Missing start: iterate till the begin (inclusive)
print(my_list[2: :-1])      # [2, 1, 0]

# covers from the end till the begin inclusive
print(my_list[ : :-1])      # [8, 7, 6, 5, 4, 3, 2, 1, 0]

# kind of: cover all values in the missing direction

# practice makes perfect :)