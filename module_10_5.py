# Домашнее задание по теме "Многопроцессное программирование".

import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding="utf-8") as file:
        while True:
            line = file.readline()
            if len(line) != 0:
                all_data.append(line)
            else:
                break
        return all_data


filenames = [f'./texts/file {number}.txt' for number in range(1, 5)]

start = datetime.datetime.now()
for name in filenames:
    read_info(name)
end = datetime.datetime.now()
print(end - start)

# if __name__ == '__main__':
#     start = datetime.datetime.now()
#     with multiprocessing.Pool() as pool:
#         pool.map(read_info, filenames)
#     end = datetime.datetime.now()
#     print(end - start)
