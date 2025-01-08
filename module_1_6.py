my_dict = {'Denis': 1991, 'Masha': 1990, 'Sasha': 1992, 'Dima': 1989}
print(my_dict)
print(my_dict['Denis'])
print(my_dict.get('Dasha'))
my_dict.update({'Dasha': 1993, 'Petya': 1994})
a = my_dict.pop('Masha')
print(a)
print(my_dict)
my_set = {1, 2, True, 'cat', False, 1, 2, (2, 3)}
print(my_set)
tuple = (4, 'dog')
my_set.update(tuple)
my_set.remove(True)
print(my_set)
