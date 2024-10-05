# Домашнее задание по теме "Try и Except".

def add_everything_up(a, b):
    if ((isinstance(a,str) and isinstance(b, int | float))
            or (isinstance(b,str) and isinstance(a, int | float))):
        return str(a) + str(b)
    else:
        return round((a + b), 3)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
