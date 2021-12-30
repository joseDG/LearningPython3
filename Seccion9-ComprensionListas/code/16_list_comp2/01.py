



lst = [1, -2, 6, -3, 2, -6]
lst3 = [n for n in lst   if n > 0]
print(lst3)     # [1, 6, 2]

lst4 = [n for n in lst   if n % 2 == 0]
print(lst4)     # [-2, 6, 2, -6]

lst5 = [n for n in lst   if n % 2 == 0 and n % 3 == 0]
print(lst5)     # [6, -6]

lst6 = [n for n in lst   if n % 2 == 0 if n % 3 == 0]
print(lst6)     # [6, -6]

sentence = 'Glad that you took this course!'
vowels = [i for i in sentence if i in 'aeiou']
print(vowels)   # ['a', 'a', 'o', 'u', 'o', 'o', 'i', 'o', 'u', 'e']

