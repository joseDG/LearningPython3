
dict = {}   # empty dict
dict[20] = 10
dict['mostafa'] = 10
dict[30] = 15
dict[(2, 7)] = 150
dict[30] = 10
# observe: values can be anything and can repeat

print(dict.keys())
# dict_keys([20, 'mostafa', 30_oop, (2, 7)])
# Starting from python 3.7 specification : the keys order is preserved (insertion order)
# However, due to several reasons, it is still best practice to not depend on that
# Maybe after 10 years. For now, if order matter: use OrderedDict
# In practice: typically u don't care about insertion order but sorted keys themselves

# Useful readings
# http://gandenberger.org/2018/03/10/ordered-dicts-vs-ordereddict/
# https://realpython.com/python37-new-features/#the-order-of-dictionaries-is-guaranteed
# https://sdrees.gitbooks.io/python-order-is-now-key/content/first-question.html
# https://stackoverflow.com/questions/1867861/how-to-keep-keys-values-in-same-order-as-declared
