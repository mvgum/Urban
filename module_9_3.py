# Домашнее задание по теме "Генераторные сборки".

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in list(zip(first, second)) if len(x) != len(y))
num = min(len(first), len(second))
second_result = (len(first[i]) == len(second[i]) for i in range(num))
print(list(first_result))
print(list(second_result))
