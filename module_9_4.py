# Домашнее задание по теме "Генераторные сборки".
from random import *

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, "a", encoding='utf-8')
        for data in data_set:
            file.write(str(data) + "\n")
        file.close()
        return
    return write_everything


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__ (self):
        text = choice(self.words)
        return text


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

