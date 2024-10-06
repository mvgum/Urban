# Домашнее задание по теме "Try и Except".

def add_everything_up(a, b):
    result = None
    try:
        result = round((a + b), 3)
    except TypeError:
        result = str(a) + str(b)
    finally:
        return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
