# Домашнее задание по теме "Потоки на классах".

from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self) -> None:
        print(f'{self.name}, на нас напали!\n')
        num_enemy = 100
        day = 0
        while num_enemy > 0:
            num_enemy -= self.power
            day += 1
            sleep(1)
            print(f'{self.name} сражается {day} день(дня)..., осталось {num_enemy} воинов.\n')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
