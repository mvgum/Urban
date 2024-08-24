# Домашняя работа по уроку "Распаковка позиционных параметров."

def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    print("__________________________________________________")


print_params(a = 1, b='строка', c=True)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [54.32, 'Строка', ["one", "two"] ]
values_dict = {'a': 25, 'b': 11,  'c': 46}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)