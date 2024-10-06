# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции".

def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for elem in numbers:
        try:
            result += elem
        except TypeError:
            incorrect_data += 1
            print("Некорректный тип данных для подсчёта суммы -", elem)
    return result, incorrect_data


def calculate_average(numbers):
    count = 0
    try:
        for _ in numbers:
            count += 1
    except TypeError:
        print("В numbers записан некорректный тип данных.")
        return None

    sum_num, incorrect_num = personal_sum(numbers)
    try:
        result = sum_num / (count - incorrect_num)
    except ZeroDivisionError:
        return 0
    return result

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
