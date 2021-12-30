# Slice with a negative step

         #-9 -8 -7 -6 -5 -4 -3 -2 -1    # 9 + neg_pos
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

sub_list = my_list[1:8:1]    # 1 2 3 4 5 6 7

sub_list = my_list[-8:-2:1]    # 1 2 3 4 5 6
sub_list = my_list[-2:-8:-1]   # 7 6 5 4 3 2

