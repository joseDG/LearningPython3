
for i in range(0, 20, 2):
    print('Given i={:2}: i^4 = {:<7} i^3 = {:^4}'.format(i, i* i * i * i, i * i * i))

"""
:7 right-aligned
:<7 left-aligned
:^7 center-aligned

Given i= 0: i^4 = 0       i^3 =  0  
Given i= 2: i^4 = 16      i^3 =  8  
Given i= 4: i^4 = 256     i^3 =  64 
Given i= 6: i^4 = 1296    i^3 = 216 
Given i= 8: i^4 = 4096    i^3 = 512 
Given i=10: i^4 = 10000   i^3 = 1000
Given i=12: i^4 = 20736   i^3 = 1728
Given i=14: i^4 = 38416   i^3 = 2744
Given i=16: i^4 = 65536   i^3 = 4096
Given i=18: i^4 = 104976  i^3 = 5832
"""