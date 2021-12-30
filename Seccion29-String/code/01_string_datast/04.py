

lst = ["Hello", "World", "Python","is", "Cool"]
first_letters = [word[0] for word in lst]
print(first_letters)    # ['H', 'W', 'P', 'i', 'C']


first_letters = [word[0].lower() for word in lst]
print(first_letters)    # ['h', 'w', 'p', 'i', 'c']


my_str = "Please 10 finds 123all dig0ts"

digits = [int(char)  for char in my_str if char.isdigit()]
print(digits)   # [1, 0, 1, 2, 3, 0]