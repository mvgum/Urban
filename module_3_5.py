# Самостоятельная работа по уроку "Рекурсия".


def get_multiplied_digits(number):
    if number == 1:
        return 1
    else:
        return number * get_multiplied_digits(number - 1)


print(get_multiplied_digits(6))
