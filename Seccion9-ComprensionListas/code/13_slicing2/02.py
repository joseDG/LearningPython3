# Slice with a negative step

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

sub_list = my_list[1:8:1]    # 1 2 3 4 5 6 7

sub_list = my_list[8:1:-1]   # 8 7 6 5 4 3 2: high to low

sub_list = my_list[7:0:-1]   # 7 6 5 4 3 2 1
sub_list = my_list[7:0:-2]   # [7, 5, 3, 1]

sub_list = my_list[2:5:-1]   # [] must be high to low

# Negative step: Missing start: default is len
sub_list = my_list[9:2:-1]      # [8, 7, 6, 5, 4, 3]
sub_list = my_list[ :2:-1]      # [8, 7, 6, 5, 4, 3]

# Negative step: Missing end: default is hmm
# starts from index 0 INCLUSIVE (NOT default)
sub_list = my_list[5: :-1]      # [5, 4, 3, 2, 1, 0]

sub_list = my_list[5:0:-1]      # [5, 4, 3, 2, 1]

sub_list = my_list[::-1]        # reversed list
# [8, 7, 6, 5, 4, 3, 2, 1, 0]

