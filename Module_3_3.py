def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

print('---------------------')

values_list =[1, 'привет', True]
values_dict = {'a': 1,'b': "строка", 'c': True}
print_params(*values_list,)
print_params(**values_dict)

print('---------------------')

values_list_2 = ['список', None]
print_params(*values_list_2, True)
