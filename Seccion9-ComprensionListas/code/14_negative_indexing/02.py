# Slice with negative indexing

         #-9 -8 -7 -6 -5 -4 -3 -2 -1    # 9 + neg_pos
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]


sub_list = my_list[3:7]     # 3 4 5 6
# we can rewrite by finding the matched -ve indices
sub_list = my_list[-6:-2]   # 3 4 5 6
sub_list = my_list[-6:7]    # 3 4 5 6
sub_list = my_list[3:-2]    # 3 4 5 6

# observe: -6 < -2
#sub_list = my_list[-2:-6]   # Empty list!

