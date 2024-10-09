# Домашнее задание по теме "Генераторные сборки".
import random
from random import *

first = 'Мама мыла раму'
second = 'Рамена мало было'

list(map(lambda x, y: x == y, first, second))


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


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
