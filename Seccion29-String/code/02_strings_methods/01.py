

print('abcDEF'.lower())        # abcdef : conver to lower letters
print('abcDEF'.upper())        # ABCDEF : conver to upper letters

print('abc'.islower())      # True : all cased characters in S are lowercase?
print('ABC'.isupper())      # True: all cased characters in S are uppercase?
print('123'.isdecimal())    # True : all characters in S are 0 to 9?

print('abcdef'.startswith('abc'))       # True
print('abcdef'.startswith('abcD'))      # False
print('abcdef'.endswith('def'))         # True

print('abcdbcd'.find('bc'))         # 1  lowest index
print('abcdbcd'.find('xx'))         # -1 if not exist
print('abcdbcd'.rfind('bc'))        # 4  highest index
#print('abcdbcd'.index('xx'))       # same as finds, but ValueError if not found

print('HiHiHi'.count('Hi'))       # 3 occurrences for Hi
print('AAAA'.count('AA'))         # 2 occurrences NOT 3

