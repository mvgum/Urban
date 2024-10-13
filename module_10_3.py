# Домашнее задание по теме "Блокировки и обработка ошибок".

import random
import threading
from threading import Thread
from time import sleep


class Bank(Thread):
    lock = threading.Lock()

    def __init__(self, balance=0):
        super().__init__()
        self.balance = balance

    def deposit(self) -> None:
        for i in range(100):
            var_d = random.randint(50, 500)
            self.balance += var_d
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {var_d}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            var_t = random.randint(50, 500)
            print(f'Запрос на {var_t}')
            if var_t <= self.balance:
                self.balance -= var_t
                print(f'Снятие: {var_t}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.locked()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
