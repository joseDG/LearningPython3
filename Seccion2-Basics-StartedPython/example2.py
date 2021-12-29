# Just create 8 variables, with suitable names for easy coding
odd1, even1, odd2, even2, odd3, even3, odd4, even4 = map(int, input().split())

even_sum = even1 + even2 + even3 + even4
odd_sum = odd1 + odd2 + odd3 + odd4

print(even_sum, odd_sum)
