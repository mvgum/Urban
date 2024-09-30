# Домашнее задание по теме "Позиционирование в файле".

def custom_write(file_name, strings):
    count = 1
    curs_dict = {}
    file = open(file_name, "a", encoding='utf-8')
    for string in strings:
        cursor = file.tell()
        key = (count, cursor)
        curs_dict[key] = string
        file.write(string)
        file.write('\n')
        count += 1
    file.close()
    return curs_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
