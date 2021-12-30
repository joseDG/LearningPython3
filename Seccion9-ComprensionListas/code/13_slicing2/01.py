# Slice with a positive step


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

sub_list = my_list[1:8  ]    # 1 2 3 4 5 6 7
sub_list = my_list[1:8:1]    # 1 2 3 4 5 6 7
sub_list = my_list[1:8:2]    # 1 3 5 7
sub_list = my_list[1:8:3]    # 1 4 7

# Missing step: default = 1
sub_list = my_list[1:8: ]   # [1, 2, 3, 4, 5, 6, 7]

# Positive step: Missing end: default is len(seq)
sub_list = my_list[1:9:2]   # 1 3 5 7
sub_list = my_list[1: :2]   # 1 3 5 7

# Positive step: Missing start: default is 0
sub_list = my_list[0:6:2]   # 0 2 4
sub_list = my_list[ :6:2]   # 0 2 4

sub_list = my_list[0:9:2]   # 0 2 4 6 8
sub_list = my_list[ : :2]   # 0 2 4 6 8

sub_list = my_list[0:9:1]   # [0, 1, 2, 3, 4, 5, 6, 7, 8]
sub_list = my_list[ : : ]   # [0, 1, 2, 3, 4, 5, 6, 7, 8]
