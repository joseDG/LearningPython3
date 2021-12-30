

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# 2 is the start
# 6 is end (exclusive): ends actually at 5
sub_list = my_list[2:6]     # 2 3 4 5

sub_list[0] = 100           # my_list is NOT changed

sub_list = my_list[5:6]     # 5 a single element

sub_list = my_list[5:1000]  # 5 6 7 8

# syntax: my_list[start : end+1
