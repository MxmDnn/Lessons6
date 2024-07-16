my_dict = {'Petr':1990, 'Pavel':1995, 'Andrey':1999, 'Zlata':2001, 'Darya':2004}
print('Dict: ',my_dict)
print('Existing value: ', my_dict['Zlata'])
print('Not existing value: ', my_dict.get('Elena'))
my_dict.update({'Lev': 2002, 'Damir': 2000})
a = my_dict.pop('Andrey')
print('Deleted value: ', a)
print('Modified dictionary: ',my_dict)
my_set={1,3,5,7,1990,1995,1999,2001,2004,2002,1995,7,3,'Zlata Petrovna','Darya Pavlovna', (7,5,3),False}
print('Set: ',my_set)
my_set.add('Lev Damirovich')
my_set.add('The end')
my_set.discard(False)
print('Modified set: ', my_set)