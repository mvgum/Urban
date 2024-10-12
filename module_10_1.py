# Домашнее задание по теме "Создание потоков".

from time import sleep
from threading import Thread


def write_words(word_count, file_name):
    count = 0
    while count != word_count:
        count += 1
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово № {count}. \n')
        sleep(0.1)
    print(f'Завершилась запись в файл {file_name}.')


thr_first = Thread(target=write_words, args=(10, "example1.txt"))
thr_second = Thread(target=write_words, args=(30, "example2.txt"))
thr_third = Thread(target=write_words, args=(200, "example3.txt"))
thr_fourth = Thread(target=write_words, args=(100, "example4.txt"))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()
