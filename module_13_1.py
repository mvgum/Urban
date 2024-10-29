# Домашнее задание по теме "Асинхронность на практике".
import asyncio
from time import sleep


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        sleep(1 / power)
        print(f'Силач {name} поднял шар номер {i + 1}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    await task_1
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    await task_2
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_3

asyncio.run(start_tournament())
